# https://docs.python.org/3/library/ftplib.html
import ftplib, os

def ftp_upload(ftp, local_filename, local_dir='', remote_filename='', remote_dir=''):
    local_file_path = os.path.join(local_dir, local_filename)
    if not os.path.isfile(local_file_path):
        print('Error: {} does not exist!'.format(os.path.abspath(local_file_path)))
        return
    init_dir = ftp.pwd()
    if remote_dir:
        ftp.cwd(remote_dir)
    if not remote_filename:
        remote_filename = local_filename
    with open(local_file_path, 'rb') as file:
        ftp.storbinary('STOR {}'.format(remote_filename), file)
    if remote_dir:
        ftp.cwd(init_dir)

# create ftp session
ftp_host = 'host'
ftp_user = 'user'
ftp_pass = 'pass'

with ftplib.FTP(ftp_host, ftp_user, ftp_pass) as ftp:
    # output all direcotries and files in stout
    # ftp.dir()

    # retrieve remote list of directory and files
    # file_list = ftp.nlst()

    # upload a file to ftp
    ftp_upload(ftp, 'test.py')
