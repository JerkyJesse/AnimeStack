/**
 * AnimeStack - DeepSeek Harness operator commands.
 *
 * The bundle companion to the AnimeStack Agent presets: registers the house's
 * slash commands globally and queues each command's prompt as one human user
 * message. That is the prompt-template behavior of the other hosts ported to
 * this host's command registry - the registry itself opens no model turn, and
 * `Agent.followup()` starts the next turn with the expanded prompt, so the
 * command lifecycle stays in the session log like any other human input.
 *
 * The prompt data lives in ./commands.generated.js, written by
 * scripts/gen-dsh-house from the public command sources and re-run into this
 * bundle whenever they move. The module is dependency-free by design: a profile
 * `link:` install must not need a second copy of any @deepseek-ai package, so
 * the one message value the plugin needs is built here in the exact shape the
 * host's own user-message factory produces ({ id, role, content, source }).
 */
import commands from "./commands.generated.js";

/** Cordis plugin identity for this row's diagnostics. */
export const name = "animestack-house-commands";
/** The command registry is the only host service this plugin consumes. */
export const inject = ["commands"];

/** The human origin of a slash-command invocation. */
const USER_SOURCE = Object.freeze({ kind: "user" });

/** Recursively freeze a value; the inbox treats published messages as immutable. */
function deepFreeze(value) {
  if (value === null || typeof value !== "object" || Object.isFrozen(value)) return value;
  Object.freeze(value);
  for (const key of Object.keys(value)) deepFreeze(value[key]);
  return value;
}

/**
 * Build the user-role message `Agent.followup()` admits: a fresh identity, one
 * text block holding the expanded command prompt, and the human source.
 * @param {string} text - expanded command prompt.
 */
function createUserMessage(text) {
  return deepFreeze(
    structuredClone({
      id: globalThis.crypto.randomUUID(),
      role: "user",
      content: [{ type: "text", text }],
      source: USER_SOURCE,
    }),
  );
}

/**
 * Expand one command template: every `$ARGUMENTS` occurrence takes the raw
 * slash-command tail, trimmed. A body with no placeholder keeps its text and
 * carries non-empty operator input as a trailing block instead of silently
 * dropping it.
 * @param {{ body: string }} spec - generated command specification.
 * @param {string} rawInput - text after the command name.
 */
function expandPrompt(spec, rawInput) {
  const args = rawInput.trim();
  if (spec.body.includes("$ARGUMENTS")) return spec.body.replaceAll("$ARGUMENTS", args);
  return args === "" ? spec.body : `${spec.body}\n\nOperator input:\n\n${args}`;
}

/**
 * Register every generated command in the global command layer.
 * @param {object} ctx - Cordis plugin context (the `commands` injection).
 */
export function apply(ctx) {
  for (const spec of commands) {
    ctx.commands.register({
      name: spec.name,
      description: spec.description,
      input: { hint: spec.hint },
      handler(invocation) {
        invocation.agent.followup(createUserMessage(expandPrompt(spec, invocation.rawInput)));
        return { kind: "success", text: `/${spec.name}: house prompt queued` };
      },
    });
  }
}
