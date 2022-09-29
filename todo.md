1. change how cursor applys to the camera pos: testbed.cu: 1335, mouse_drag -- Done
2. calculate graidents for geometry loss in regnerf
3. modify functions that sample a patch of pixels instead of single pixel
   1. generate_training_samples_nerf: testbed_nerf.cu: 1049
   2. compute_loss_kernel_train_nerf: testbed_nerf.cu: 1563
   3. train_nerf_step: testbed_nerf.cu: 3001
4. write my own functions
   1. image_idx_regnerf: generate image index for each patch
   2. generate_training_patches_regnerf: output patch_pos (float: img, x, y)
   3. generate_training_samples_regnerf
   4. compute_loss_kernel_train_regnerf
   5. train_regnerf_step

patch size: 1-16, so max pixel num is 256, reasonable for a thread block

regnerf buffers:
1. patch_pos (global): record img id and xy position
2.  (shared)