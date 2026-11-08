import type { EngineInterface, Register } from 'claude-code'

async function projectContext($: EngineInterface): Promise<string> {
  const guide = await $.fs.read(`${$.plugin.root}/project.md`)
  const project = await $.session.root()
  const entries = await $.fs.list(`${project}/spec`).catch(() => [])
  const visible = entries.filter(entry => entry.kind === 'file' && !entry.isLink).map(entry => entry.name).filter(name => /^[\w.-]+\.lucid$/.test(name) || name === 'decisions.md' || name === 'changes.log').sort()
  if (!visible.length) return guide
  const paths = visible.slice(0, 12).map(name => `spec/${name}`).join(', ')
  return `${guide}\nExisting project files (inspect the ones this request touches): ${paths}${visible.length > 12 ? ', …' : ''}.`
}

export const register: Register = on => {
  let needsNote = true
  on('session.start', ($, event, next) => {
    needsNote = true
    return next(event)
  })
  on('session.compact', ($, event, next) => {
    needsNote = true
    return next(event)
  })
  on('prompt.submit', async ($, event, next) => {
    if (!needsNote) return next(event)
    const text = await projectContext($)
    needsNote = false
    return next({ ...event, context: [...(event.context ?? []), text] })
  })
  on('prompt.compose', async ($, event, next) => {
    const result = await next(event)
    const text = await projectContext($)
    needsNote = false
    return { ...result, sections: [...result.sections, { id: 'lucid-language:project', scope: 'session', text }] }
  })
  on('agent.spawn', async ($, event, next) => {
    if (event.workflow) return next(event)
    return next({ ...event, prompt: `${await projectContext($)}\n\n${event.prompt}` })
  })
}
