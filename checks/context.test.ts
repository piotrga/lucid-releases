import type { On } from 'claude-code'
import { expect, mock, test } from 'claude-code/testing'

const MODEL = { model: 'test', promptModel: 'test', surfaces: ['terminal' as const], tools: [], outputStyle: null, traits: [] }

function fixture(on: On) {
  mock.session(on)
  const notes: string[][] = []
  on('session.root', () => ({ value: '/fixture' }))
  on('fs.read', () => ({ value: 'Read agreed requirements first.' }))
  on('fs.list', () => ({ value: ['stock.lucid', 'decisions.md', 'scratch.txt'].map(name => ({ name, kind: 'file' as const, size: 1, mtimeMs: 1, isLink: false })) }))
  on('session.compact', ($, event) => ({ messages: event.messages }))
  on('session.start', ($, event) => ({ cwd: event.cwd }))
  on('prompt.compose', () => ({ sections: [] }))
  on('prompt.submit', ($, event) => { notes.push([...(event.context ?? [])]); return { text: event.text } })
  return notes
}

test('project requirements reach requests and are restored after compaction', async ($, on) => {
  const notes = fixture(on)
  await $.session.start({ cwd: '/fixture', surface: 'terminal', isInteractive: true })
  const submit = () => $.prompt.submit({ text: 'Review stock', wait: false })
  await submit()
  await submit()
  await $.session.compact({ messages: [{ role: 'user', text: 'Review stock', toolUses: [], toolResults: [] }] } as never)
  await submit()
  expect(notes[0].join(' ')).toContain('spec/stock.lucid')
  expect(notes[1]).toEqual([])
  expect(notes[2]).toEqual(notes[0])
  const result = await $.prompt.compose(MODEL)
  const text = result.sections.find(section => section.id === 'lucid-language:project')?.text ?? ''
  expect(text).toContain('spec/decisions.md')
  expect(text).not.toContain('scratch.txt')
})

test('delegated work receives the specification context and the original task', async ($, on) => {
  fixture(on)
  let prompt = ''
  on('agent.spawn', ($, event) => { prompt = event.prompt; return { agentId: 'worker', model: 'test' } })
  await $.agent.spawn({ tool_use_id: 'w', description: 'Review', prompt: 'Check stock boundaries' } as never)
  expect(prompt).toContain('spec/stock.lucid')
  expect(prompt).toContain('Check stock boundaries')
})
