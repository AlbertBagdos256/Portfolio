def get_users_avatars(users):
    img_list = []
    i = 0
    for user in users:
        img_path = '../static/images/users_avatars/' + user.image_file
        img_list.append(img_path)
        i+=1
        if i == 6:
            break
    return img_list

def get_users_urls(users):
    users_urls = []
    i = 0
    for user in users:
        main_path = '/user/' + user.username
        users_urls.append(main_path)
        i+=1
        if i == 6:
            break
    return users_urls
    
def get_main_list(images_list, users_urls):
    support_list = []
    final_list   = []
    
    for i in range(int(len(images_list))):
        support_list.append(images_list[i])
        support_list.append(users_urls[i])
        final_list.append(support_list)
        i+=1
        support_list = []
        
    return final_list
        