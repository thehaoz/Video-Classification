from sklearn.model_selection import train_test_split
import os
import cv2

###################


def preprocess_videos(root_dir, folder, dataset_name = "hmdb51"):
    extension = ".avi"
    n_frames = 16
    data_train_dir = os.path.join(root_dir, dataset_name)
    if not os.path.exists(os.path.join(root_dir,dataset_name)):
        data_train_dir = os.path.join(root_dir, dataset_name)
        os.mkdir(data_train_dir)
        os.mkdir(os.path.join(data_train_dir, "train"))
        os.mkdir(os.path.join(data_train_dir, "val"))
        os.mkdir(os.path.join(data_train_dir, "test"))
    
    target_folder_dir = os.path.join(root_dir, folder)
    classes = sorted(os.listdir(target_folder_dir))

    for class_names in classes:

        class_videos = os.listdir(os.path.join(target_folder_dir, class_names))
        train_val_videos, test_videos = train_test_split(class_videos, test_size=0.2, random_state=42)
        train_videos, val_videos = train_test_split(train_val_videos, test_size=0.2, random_state=42)
        
        for train_vid_names in train_videos:
            if extension not in train_vid_names:
                continue
            path2vid = os.path.join(target_folder_dir, class_names, train_vid_names)
            frames, vlen = get_frames(path2vid, n_frames = n_frames)
            vid_name = path2vid.replace(extension, "")
            vid_name = vid_name.split("\\")[-1]
            path2store = os.path.join(data_train_dir, "train", class_names, vid_name )
            if not os.path.exists(os.path.join(data_train_dir, "train", class_names)):
                os.mkdir(os.path.join(data_train_dir, "train", class_names))
            if not os.path.exists(path2store):
                os.mkdir(path2store)
            store_frames(frames, path2store)
            
        for val_vid_names in val_videos:
            if extension not in val_vid_names:
                continue
            path2vid = os.path.join(target_folder_dir, class_names, val_vid_names)
            frames, vlen = get_frames(path2vid, n_frames = n_frames)
            vid_name = path2vid.replace(extension, "")
            vid_name = vid_name.split("\\")[-1]
            path2store = os.path.join(data_train_dir, "val", class_names, vid_name )
            if not os.path.exists(os.path.join(data_train_dir, "val", class_names)):
                os.mkdir(os.path.join(data_train_dir, "val", class_names))
            if not os.path.exists(path2store):
                os.mkdir(path2store)
            store_frames(frames, path2store)
            
        for test_vid_names in test_videos:
            if extension not in test_vid_names:
                continue
            path2vid = os.path.join(target_folder_dir, class_names, test_vid_names)
            frames, vlen = get_frames(path2vid, n_frames = n_frames)
            vid_name = path2vid.replace(extension, "")
            vid_name = vid_name.split("\\")[-1]
            path2store = os.path.join(data_train_dir, "test", class_names, vid_name )
            if not os.path.exists(os.path.join(data_train_dir, "test", class_names)):
                os.mkdir(os.path.join(data_train_dir, "test", class_names))            
            if not os.path.exists(path2store):
                os.mkdir(path2store)
            store_frames(frames, path2store)            


def store_frames(frames, path2store):
    for ii, frame in enumerate(frames):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  
        path2img = os.path.join(path2store, "frame"+str(ii)+".jpg")
        cv2.imwrite(path2img, frame)       

def get_frames(filename, n_frames= 1):
    frames = []
    v_cap = cv2.VideoCapture(filename)
    v_len = int(v_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_list= np.linspace(0, v_len-1, n_frames+1, dtype=np.int16)
    
    for fn in range(v_len):
        success, frame = v_cap.read()
        if success is False:
            continue
        if (fn in frame_list):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
            frames.append(frame)
    v_cap.release()
    return frames, v_len   