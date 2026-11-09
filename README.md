# Inferium Lab

An experimental crop mod for Horizon 26.3. Plant Inferium Seeds on ordinary farmland and harvest Inferium Essence when the crop reaches age 7. The crop returns a seed at every age and refuses ordinary bone meal.

## Build and install

This native source mod targets [Horizon Nightly 66f3981](https://github.com/horizon-rust/horizon/tree/66f3981f522b24c250b21523a70080965b940424) and [Horizon Mixins e8cd0aa](https://github.com/horizon-rust/horizon-mixins/tree/e8cd0aa38cffef49cb2e088ef716baa107148c02). The bundle pins both revisions so the Launcher can build the matching game.

```sh
python tools/package.py
cargo horizon-mod check target/inferium_lab-0.1.0.hnmod
```

Import `target/inferium_lab-0.1.0.hnmod` as a native mod in Horizon Launcher and build the instance. Start with a new world and use `/give @s inferium_lab:inferium_seeds` to get the prototype's seeds. The package refers to the game's existing wheat and redstone models.

The bundle uses the native block, item, loot and bone-meal hooks. Two targeted mixins bind the seed to the crop and make creative pick block select it on the pinned game revision.

## Validation

All ten checks passed on Windows with the pinned source staged by Horizon Mixins and compiled with Rust 1.99.1 (MSVC). The game ran headless with its integrated server in a disposable world.

| Check | Observed result |
| --- | --- |
| Survival placement on farmland | Three age-0 crops, one seed consumed per placement. |
| Survival placement on dirt | No crop and no seed consumed. |
| Growth | Inferium and wheat reached age 7 with random tick speed set to 1024. |
| Harvest | One seed at age 0. One seed and one essence at age 7. |
| Creative pick block | Selected the Inferium seed. |
| Ordinary bone meal by hand and dispenser | Inferium stayed at age 0 and kept all three units. Wheat grew and used one unit in each control. |

The official `cargo horizon-mod check` accepted the native package. SHA-256 `e05c584fdb5f9caeb67f6a53eb62c71cbc137b4c463c6ee01902509d9624f027`.

## Credits

Inferium Lab uses original Rust and JSON. The crop behavior was compared with BlakeBr0's MIT-licensed Mystical Agriculture and its Inferium Seeds documentation. The attribution and reference license are included in the bundle's `NOTICE`. [Mystical Agriculture](https://github.com/BlakeBr0/MysticalAgriculture) · [Java reference](https://github.com/BlakeBr0/MysticalAgriculture/blob/3478be1900dfd608b480d3a58434f54d87ff26cd/src/main/java/com/blakebr0/mysticalagriculture/block/InferiumCropBlock.java#L21-L59) · [Inferium Seeds](https://blakesmods.com/wiki/mysticalagriculture/items/inferium-seeds)
