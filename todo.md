1. change how cursor applys to the camera pos: testbed.cu: 1335, mouse_drag -- Done
2. calculate graidents for geometry loss in regnerf
3. use s instead of t as the m in dist loss, define s
4. malloc gpu mem for the computation of cumsum of w and w*m
5. calculate distortion loss and its grad