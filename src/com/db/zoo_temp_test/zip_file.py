'''
Created on Jan 15, 2015

@author: jiefeng
'''
import os.path
import zipfile

from com.db.conf import Conf
from com.db.library.Log import stamp_datetime_co


def zip_dir(dirname, zipfilename):
    '''
        :Purpose: Zip directory or file
        
        :Parameter: 
            dirname :     directory should be archived
            zipfilename : the output zip file name
        
        :return:
            None
            
        :uasge: 
            zip_dir(Conf.RESULT_PATH,
                    "%s\\%s_%s.zip" % (Conf.RESULT_PATH, Conf.LOG_FILES, stamp_datetime_co()))
        '''
    
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
    
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        print arcname
        zf.write(tar,arcname)
    zf.close()
 
 
def unzip_file(zipfilename, unziptodir):
    """ do not verify
    """
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\','/')
        
        if name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name))
        else:            
            ext_filename = os.path.join(unziptodir, name)
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir) : os.mkdir(ext_dir,0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()
 
if __name__ == '__main__':
    print '%s\\%s_%s.zip' %(Conf.RESULT_PATH, Conf.LOG_FILES, stamp_datetime_co())
    zip_dir(Conf.RESULT_PATH,
            "%s\\%s_%s.zip" % (Conf.RESULT_PATH, Conf.LOG_FILES, stamp_datetime_co()))
#     unzip_file(r'E:/python/learning/zip.zip',r'E:/python/learning2')