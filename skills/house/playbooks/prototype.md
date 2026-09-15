# Prototype

## When

- "spike this idea"
- "does this approach even work"
- throwaway exploration before any real build

## The loop

Lead: Yui.

- **Yui** — What wound does this exploit? BUILD the throwaway fast, from a named data shape, no production harness. Write the falsifier even here. Produces the prototype and its verdict.
- **Niko** — Where does it live, and what must it never touch? The prototype lives in a scratch directory; it never touches production state. Produces the quarantine.
- **Rin** — How is this allowed to die? The death is the prototype leaking into the real path. Produces ACCEPT or END on the quarantine.
- **Reika** — What are we allowed to want? Close: does the idea earn a real build, or does it die here. `VERDICT: ...`.

## Gates

- The prototype is throwaway and is never shipped as-is.
- It touches nothing outside its scratch directory.
- The falsifier is written, so the prototype has a kill sentence before it has a victory lap.

## Close

Reika closes: `VERDICT: ...` — promote to a feature, or bury.

## Notes

A prototype is a question, not a product. It never ships; it earns a real build or it is thrown away. The grave is free here — cheaper to bury a prototype than to maintain one.
