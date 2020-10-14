# Video-Classification

# Description

This project works on action recognition using deep learning framework. Will be making use of HMDB51 dataset [link here](https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/#Downloads) that contains 51 action classes.

---

## Utilities Folder
Contains `Video_utils.py` that is used to process video frames into its individual frames


`preprocess_videos(root_dir, folder, dataset_name = "hmdb51")` splits the video into N frames (default 16 frames), stored in individual class folder

