Non Photorealistic Rendering <br>
openCV project #3<br>
The image used can be found at [Link](https://github.com/Sidhved/MyMachineGotEyes/blob/main/NonPhotorealisticRendering/Amy.jpg)

-> edgePreservingFilter : As the name suggests, preserves edges<br>
-> RECURS_FILTER : recursive filter<br>
-> NORMCONV_FILTER : Normalised Convolution Filter<br>
-> detailEnhance : Enhances details of a particular image<br>
    -> src : i/p 8-bit 3-channel img<br>
    -> dst : O/p img with same size and type as src<br>
    -> sigma_s : Range between 0 to 200<br>
    -> sigma_r : Range between 0 to 1<br>
-> pencilSketch : Pencil-like non-photorealistic line drawing(parameters similar to detailEnhance but has shade_factor range from 0 to 0.1)
-> stylization : aims to produce digital imagery with a wide variety of effects not focused on photorealism. Edge-aware filters are ideal for stylization, as they can abstract regions of low contrast while preserving, or enhancing, high-contrast features.
