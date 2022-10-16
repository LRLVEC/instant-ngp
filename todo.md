# 1. Todo
1. change how cursor applys to the camera pos: testbed.cu: 1335, mouse_drag -- Done
2. use s instead of t as the m in dist loss, define s -- Done
3. malloc gpu mem for the computation of cumsum of w and w*m -- Done
4. calculate distortion loss and its grad -- Done
5. add opacity loss -- Done
6. add random rays starting from positions outside the aabb -- Done
   1. add function generate_extra_training_samples_nerf -- Done
   2. add function compute_extra_ray_loss_kernel_train_nerf -- Done
   3. add function train_extra_nerf_step -- Done
   4. modify fucntion train_nerf -- Done
7. test the effect of dist loss and opacity loss, compare with native ngp
   1. render full images and video for test
   2. calculate psnr
8. change 2 optimizer_step calls into 1 in function train_nerf()
9.  change opacity loss to see effects

# Ideas
1. add unbounded scene encoding as mipnerf360 for ngp?
2. add decay for distortion loss scale and opacity loss scale so they may converge faster?
   1. no, use 0.01 for distortion loss scale and 0.001 for opacity loss scale constantly
   2. otherwise, they effect of the loss will decay
3. sample extra rays according to the density grid may be helpful?
   1. not very necessary since the sample num is the same
