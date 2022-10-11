1. change how cursor applys to the camera pos: testbed.cu: 1335, mouse_drag -- Done
2. use s instead of t as the m in dist loss, define s -- Done
3. malloc gpu mem for the computation of cumsum of w and w*m -- Done
4. calculate distortion loss and its grad -- Done
5. add opacity loss -- Done
6. add random rays starting from positions outside the aabb
