import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def exists(self, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        dropboxPath = dbx.files_get_metadata(file_to)
        if dropboxPath:
            i = 0
            for file in dbx.files_list_folder('/enregistrements').entries:
                if file.name.find(file_to):
                    if i < 10:
                        if file_to + str(0) + str(i) != file.name:
                            dropboxPath = False
                            file_to = file_to + str(0) + str(i)
                    else:
                        if file_to + str(i) != file.name:
                            dropboxPath = False
                            file_to = file_to + str(i)
                    i = i + 1
        return file_to

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        file_to = self.exists(file_to)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

    def file_name_songs(self):
        dbx = dropbox.Dropbox(self.access_token)

        i = 1
        for file in dbx.files_list_folder('/chansons').entries:
            print(i, end=". ")
            print(file.name)
            i = i + 1

    def file_name_recording(self):
        dbx = dropbox.Dropbox(self.access_token)

        i = 1
        for file in dbx.files_list_folder('/enregistrements').entries:
            print(i, end=". ")
            print(file.name)
            i = i + 1


