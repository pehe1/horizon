use mod_api::{
    BlockPart, Hooks, IsValidBonemealTargetEvent, LevelSide, Registrar, RegistrationContext,
};

#[derive(Default)]
struct Mod;

struct InferiumCrop;

#[mod_api::horizon_part]
impl BlockPart for InferiumCrop {
    fn is_valid_bonemeal_target(
        &self,
        _: LevelSide<'_>,
        _: &mut IsValidBonemealTargetEvent,
    ) -> Option<bool> {
        Some(false)
    }
}

#[mod_api::horizon_mod]
impl Hooks for Mod {
    fn register(&self, registrar: &mut dyn Registrar, _: &RegistrationContext) {
        let crop = registrar.block_key("inferium_lab:inferium_crop");
        registrar.block_part(crop, InferiumCrop);
    }
}
