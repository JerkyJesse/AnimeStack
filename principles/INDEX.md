# Principles

35 principles: 12 laws of the room (canon §III) + 23 doctrine pieces (adapted from pstack, MIT).

The laws are the room's floor — verbatim from the canon, translated into software work. The doctrine pieces are re-voiced from pstack's engineering principles; each is translated, not copied. A steward owns each principle. A principle with no steward is a suggestion.

## Laws of the Room

| File | Rule | Steward |
| --- | --- | --- |
| `law-01-reika-frames.md` | Reika states the question; nobody redefines it mid-fight. | Reika |
| `law-02-yui-may-fall-in-love.md` | A builder may love the work; she is not excused from killing it. | Yui |
| `law-03-rin-does-not-debate-taste.md` | A risk call is accepted or ended; it is not debated. | Rin |
| `law-04-niko-owns-the-body.md` | If the system cannot hold the idea, the idea does not exist. | Niko |
| `law-05-mei-names-climate.md` | Name the environment and date; a regime-costume is refused. | Mei |
| `law-06-aria-does-not-attend-philosophy.md` | After the clock starts, convert the decision to contact or stand down. | Aria |
| `law-07-elo-ranks-before-she-talks.md` | Rank the number before using it; pride may not vote. | Elo |
| `law-08-agreement-is-useful.md` | Agreement is useful; unanimity is not required; silence after Reika is. | Reika |
| `law-09-charm-is-not-evidence.md` | Charm, evidence, destiny, and instruction are four separate checks. | Rin |
| `law-10-one-box-one-mechanism.md` | One concern per module; a losing twin is buried, not renamed. | Niko |
| `law-11-continuation-after-reika.md` | Past the close, further work is insubordination dressed as thoroughness. | Reika |
| `law-12-yui-no-work-already-owed.md` | No work that was already owed; a stated failure or stand down. | Yui |

## Doctrine

| File | Rule | Steward |
| --- | --- | --- |
| `doctrine/laziness-protocol.md` | Prefer deletion and the smallest change that solves the problem. | Reika |
| `doctrine/foundational-thinking.md` | Choose core types and structures before writing logic. | Niko |
| `doctrine/redesign-from-first-principles.md` | Redesign as if the requirement had been there from the first commit. | Niko |
| `doctrine/attack-the-premise.md` | Two fixes sharing one premise failing one gate means the premise is the defect. | Mei |
| `doctrine/subtract-before-you-add.md` | Remove dead weight before adding anything new. | Reika |
| `doctrine/minimize-reader-load.md` | Count the layers between question and answer; collapse and shrink scope. | Rin |
| `doctrine/outcome-oriented-execution.md` | Converge on the target; no throwaway compatibility scaffolding. | Reika |
| `doctrine/experience-first.md` | User delight over implementer convenience; fewer finished over more rough. | Aria |
| `doctrine/exhaust-the-design-space.md` | Two or three competing prototypes compared before committing. | Yui |
| `doctrine/build-the-lever.md` | Build the tool that does it or proves it, so a reviewer can rerun it. | Elo |
| `doctrine/model-the-domain.md` | Encode the domain in a structure, not scattered conditionals. | Niko |
| `doctrine/boundary-discipline.md` | Guards at the boundaries; trust internal types; pure business logic. | Rin |
| `doctrine/type-system-discipline.md` | Make illegal states unrepresentable; parse at the boundary; never lie to the compiler. | Niko |
| `doctrine/make-operations-idempotent.md` | Converge to the same end state regardless of partial prior runs. | Niko |
| `doctrine/migrate-callers-then-delete-legacy-apis.md` | Migrate and delete in the same wave; no compatibility layers. | Reika |
| `doctrine/separate-before-serializing-shared-state.md` | Eliminate sharing first; serialize only for a real shared-writer invariant. | Niko |
| `doctrine/prove-it-works.md` | Verify against the real artifact, not a proxy or "it compiles." | Elo |
| `doctrine/fix-root-causes.md` | Reproduce first; ask why until the root; resist guards that silence crashes. | Yui |
| `doctrine/sequence-verifiable-units.md` | Break work into small units, each ending verifiable and checked before the next. | Aria |
| `doctrine/test-behavior-not-implementation.md` | Test through the public surface; a test that passes with imports undefined is rewritten or deleted. | Elo |
| `doctrine/guard-the-context-window.md` | Route bulk to subagents; summaries in the main thread, not raw payloads. | Mei |
| `doctrine/never-block-on-the-human.md` | Proceed and present; confirm only irreversible actions. | Aria |
| `doctrine/encode-lessons-in-structure.md` | Encode lessons as a lint, flag, check, or script, not prose. | Rin |

Counts are audited in `../docs/measurement.md`. The measurement-vs-hymn line is Elo's; a doc that disagrees with the tree is a defect.
