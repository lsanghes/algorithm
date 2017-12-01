import sys, ftplib, os, datetime, time
class FTP_library:
    def __init__(self, ftp):
        self.start_time = time.time()
        self.ftp = ftp
        self.files1 = set()
        self.files2 = set()

    def get_file_name(self, line):
        return line.split()[8]

    def register1(self, line):
        self.files1.add(line)

    def register2(self, line):
        self.files2.add(line)

    def is_file_stable(self):
        return self.files1 == self.files2

    def check_timeout(self):
        # terminate the script if exceeded max_run_duration
        if self.max_run_duration and time.time() - self.start_time > self.max_run_duration:
            sys.exit('Error: exceeded max runtime of {} seconds'.format(self.max_run_duration))

    def check_availability(self):
        self.ftp.dir(self.remote_file_name, self.register1)
        while not self.files1:
            self.check_timeout()
            print('{}: Files are not available, retrying in {} seconds'.format(
                datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.availability_interval))
            time.sleep(self.availability_interval)
            self.ftp.dir(self.remote_file_name, self.register1)
        print('{}: Files are available'.format(
            datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')))
        for line in self.files1:
            print(line)

    def check_stability(self):
        print('{}: Waiting for {} seconds to check file stability'.format(
            datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.stability_interval))
        time.sleep(self.stability_interval)
        self.ftp.dir(self.remote_file_name, self.register2)
        while not self.is_file_stable():
            # print([self.files1, self.files2])
            self.check_timeout()
            print('{}: Files are not stable, retrying in {} seconds'.format(
                datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), self.stability_interval))
            self.files1, self.files2 = self.files2, set()
            time.sleep(self.stability_interval)
            self.ftp.dir(self.remote_file_name, self.register2)
        print('{}: Files are stable, retrieving files'.format(
            datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')))
        for line in self.files1:
            print(line)

    def ftp_stable_download(self, remote_file_name, remote_dir='', local_file_name='',
        local_dir='', availability_interval=300,
        stability_interval=60, max_run_duration=0):

        self.remote_file_name = remote_file_name
        self.availability_interval = int(availability_interval)
        self.stability_interval = int(stability_interval)
        self.max_run_duration = int(max_run_duration)

        # nagivate to the remote dir if defined
        if remote_dir:
            self.ftp.cwd(remote_dir)

        # check if files are available
        self.check_availability()

        # check if files are stable
        if stability_interval:
            self.check_stability()

        # files are both available and stable, begin download
        for line in self.files1:
            fname = local_file_name if local_file_name else self.get_file_name(line)
            local_file_path = os.path.join(local_dir, fname)
            self.ftp.retrbinary('RETR ' + fname, open(local_file_path, 'wb').write)
            print('{}: {} has been transfered successfully'.format(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), fname))

        # close ftp connection
        self.ftp.quit()

cmdargs = sys.argv
args_ftphost = cmdargs[1]
args_ftpuser = cmdargs[2]
args_ftppass = cmdargs[3]
args_remote_file = cmdargs[4]

# https://docs.python.org/3/library/ftplib.html
ftp = ftplib.FTP(args_ftphost, args_ftpuser, args_ftppass)
ftp_lib = FTP_library(ftp)
if len(cmdargs) == 5:
    ftp_lib.ftp_stable_download(args_remote_file)
elif len(cmdargs) == 11:
    args_remote_path = cmdargs[5]
    args_local_file = cmdargs[6]
    args_local_path = cmdargs[7]
    args_retry_interval = cmdargs[8]
    args_stability_duration = cmdargs[9]
    args_max_runtime = cmdargs[10]
    ftp_lib.ftp_stable_download(args_remote_file, args_remote_path, args_local_file,
        args_local_path, args_retry_interval, args_stability_duration, args_max_runtime)
else:
    print("ERROR: incorrect number of parameters")
    exit()

# test cases
# python C:\Users\ssang\algorithm\mylib\FTPStableDownload.py host user pass *MQexplorer_7502_windows* "" "" "C:\Users\ssang\Downloads" 30 45 60
# python C:\Users\ssang\algorithm\mylib\FTPStableDownload.py host user pass Asia_Final_Short_Batch_Statement20170206* "" "" "C:\Users\ssang\Downloads" 5 10 60
# python C:\Users\ssang\algorithm\mylib\FTPStableDownload.py host user pass Asia_Final_Short_Batch_Statement20170206* "" "" "C:\Users\ssang\Downloads" 5 10 60
# python C:\Users\ssang\algorithm\mylib\FTPStableDownload.py host user pass MQexplorer_7502_windows* "" "" "C:\Users\ssang\Downloads" 5 10 60
# python C:\Users\ssang\algorithm\mylib\FTPStableDownload.py host user pass CROS_TEST_20161204.csv* "" "" "" 5 10 60
# python C:\Users\ssang\algorithm\mylib\FTPStableDownload.py host user pass CROS_TEST_20161204.csv*
