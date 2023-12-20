import os, shutil

path = "./test"
d_path = "./images"

def batch_move_and_rename(s_path, d_path, prefix):
    count = 0
    for fname in os.listdir(s_path):
        old_fname = os.path.join(s_path, fname)
        new_fname = os.path.join(s_path, prefix+fname)
        os.rename(old_fname, new_fname)
        shutil.move(new_fname, d_path)
        count = count + 1
    return count    
        
if not os.path.isdir(d_path):
    os.mkdir(d_path)
    
a = batch_move_and_rename(path+"/圖片1", d_path, "a_")
b = batch_move_and_rename(path+"/圖片2", d_path, "b_")        
c = batch_move_and_rename(path+"/圖片3", d_path, "c_")
d = batch_move_and_rename(path+"/圖片4", d_path, "d_")
shutil.rmtree(path)
print("總共更名和搬移: ", a+b+c+d, "個檔案...")
