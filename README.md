# Inferium Lab

An experimental crop mod for the `arismoko/horizon` fork. This is one crop inspired by Mystical Agriculture. The prototype targets the fork's mod API at `de9f0ebdefc2fed1333d84a411e333a3adf856e1`. The official Horizon launcher and registry have not been validated for this package. [Tested Horizon revision](https://github.com/arismoko/horizon/tree/de9f0ebdefc2fed1333d84a411e333a3adf856e1)

## Build

Place the pinned fork checkout beside this source directory under the name `horizon-mystical-agriculture`. Use Rust 1.99.1 with `rust-src` and `wasm32-unknown-unknown` and use `cargo horizon-mod` from that checkout. The tool generates `mod.wasm` and writes its hash into the package manifest.

```sh
cargo horizon-mod build --wasm
cargo horizon-mod check target/horizon-mod/inferium_lab.hmod
```

For a locally built game, generate `horizon-wasm-std.wasm` next to its executable with `cargo horizon-mod wasm-std <output>`. The Windows build used a local packager fix for the process command-line limit. Start the pinned game in a disposable directory with `--dev-mod <path-to-hmod>`.

## Windows playtest

| Check | Observed result |
| --- | --- |
| Plant on ordinary farmland | Three survival placements produced age-0 plants and consumed one seed each. |
| Plant on dirt | The block stayed air and the seed count stayed at five. |
| Random growth | Inferium and wheat reached age 7 with random tick speed set to 1024. |
| Harvest at age 0 | One Inferium seed. |
| Harvest at age 7 | One Inferium seed and one Inferium Essence. |
| Creative pick block | The crop selected its seed. |
| Ordinary bone meal by hand and dispenser | Inferium stayed at age 0 and kept all three units in both tests. Wheat grew and used one unit each time. |

The reference for ordinary farmland and harvest was BlakeBr0's MIT-licensed `InferiumCropBlock.java`. The bone-meal rule follows the official mod wiki. The prototype contains original Rust and JSON with references to vanilla models. [Java reference](https://github.com/BlakeBr0/MysticalAgriculture/blob/3478be1900dfd608b480d3a58434f54d87ff26cd/src/main/java/com/blakebr0/mysticalagriculture/block/InferiumCropBlock.java#L21-L59) · [Reference license](https://github.com/BlakeBr0/MysticalAgriculture/blob/3478be1900dfd608b480d3a58434f54d87ff26cd/LICENSE) · [Inferium Seeds](https://blakesmods.com/wiki/mysticalagriculture/items/inferium-seeds)
