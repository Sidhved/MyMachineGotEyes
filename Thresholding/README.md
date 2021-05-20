Thresholding<br>
OpenCV project #2<br>
Image used can be found at [Link]()

-> IMREAD_GRAYSCALE :  If set, always convert image to the single channel grayscale image (codec internal conversion).<br>
-> THRESH_BINARY : basic binary i.e. sets to either min value or max value<br>
-> THRESH_BINARY_INV : destination is set to zero and source is set to max value i.e. opposite of binary thresholding.<br>
-> THRESH_TRUNC : destination px set to thresh if source px > threshold. otherwise set to source px val (maxVal is ignored)<br>
-> THRESH_TOZERO : dest px is set to source ox value if source px > threshold. Otherwise, set to zero (maxValue ignored)<br>
-> THRESH_TOZERO_INV : dest px is set to zero if source px > threshold. Otherwise set to source px value(maxValue is ignored). Opposite of THRESH_TOZERO<br>