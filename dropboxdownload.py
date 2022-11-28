# import dropbox as dropbox
#
# dropbox_file_name = dropbox_file_path.split('/')[-1]
# dropbox_file_path = '/'.join(dropbox_file_path.split('/')[:-1])
# dbx = dropbox.DropboxTeam(access_token)
#     # get the team member id for common user
# members = dbx.team_members_list()
# for i in range(0,len(members.members)):
#         if members.members[i].profile.name.display_name == logged_user_name:
#             member_id = members.members[i].profile.team_member_id
#             break
#     # connect to dropbox with member id
# dbx = dropbox.DropboxTeam(access_token).as_user(member_id)
#     # list all the files from the folder
# result = dbx.files_list_folder(dropbox_file_path, recursive=False)
#     #  download given file from dropbox
# for entry in result.entries:
#         if isinstance(entry, dropbox.files.FileMetadata):
#             if entry.name == dropbox_file_name:
#                 dbx.files_download_to_file(local_folder_name+entry.name, entry.path_lower)
#                 return True
# return False
# except Exception as e:
#     print(e)
#     return False