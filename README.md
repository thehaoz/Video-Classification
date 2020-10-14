# Video-Classification

# Description

This project works on action recognition using deep learning framework. Will be making use of HMDB51 dataset [link here](https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/#Downloads) that contains 51 action classes.

---

## Utilities Folder
Contains `Video_utils.py` that is used to process video frames into its individual frames


`preprocess_videos(root_dir, folder, dataset_name = "hmdb51")` splits the video into N frames (default 16 frames), stored in individual class folder
```
hmdb51/
├── test/
│   ├── brush_hair/
│   │   ├── April_09_brush_hair_u_nm_np1_ba_goo_0/
│   │   │   ├── frame0.jpg
│   │   │   ├── frame1.jpg
│   │   │   ├── frame10.jpg
|   |   |   ......
│   │   ├── atempting_to_brush_my_hair_brush_hair_u_nm_np2_le_goo_1/
│   │   │   ├── frame0.jpg
|   |   |   |...
|   |   |...
│   ├── cartwheel/
│   │   ├── (Rad)Schlag_die_Bank!_cartwheel_f_cm_np1_le_med_0/
│   │   │   ├── frame0.jpg
|   |...
├── train/
│   ├── brush_hair/
│   │   ├── April_09_brush_hair_u_nm_np1_ba_goo_2/
│   │   │   ├── frame0.jpg
│   │   │   ├── frame1.jpg
│   │   │   ├── frame10.jpg
|   |   |   |...
|   |   |...
|   |...
└── val/
    ├── brush_hair/
    │   ├── April_09_brush_hair_u_nm_np1_ba_goo_1/
    │   │   ├── frame0.jpg
    │   │   ├── frame1.jpg
    │   │   ├── frame10.jpg
    │   ├── Aussie_Brunette_Brushing_Hair_II_brush_hair_u_nm_np2_le_goo_1/
    │   │   ├── frame0.jpg

```
