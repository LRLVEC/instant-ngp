1. change how cursor applys to the camera pos: testbed.cu: 1335, mouse_drag -- Done
2. calculate graidents for geometry loss in regnerf
3. write functions that sample a patch of pixels instead of single pixel
   1. generate_training_samples_nerf: testbed_nerf.cu: 1049
   2. compute_loss_kernel_train_nerf: testbed_nerf.cu: 1563