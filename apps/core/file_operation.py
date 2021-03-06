import os.path
import pickle
import shutil
import os
from datetime import datetime
from apps.core.logger import Logger

class FileOperation:

    def __init__(self,run_id,data_path,mode):
        self.run_id = run_id
        self.data_path = data_path
        self.logger = Logger(self.run_id, 'FileOperation', mode)


    def save_model(self,model,file_name):
        try:
            self.logger.info('Start of Save Models')
            path = os.path.join('apps/models/',file_name)
            if os.path.isdir(path):
                shutil.rmtree('apps/models')
                os.mkdir(path)
            else:
                os.mkdir(path)
                with open(path + '/' + file_name+'.sav','wb') as f:
                    pickle.dump(model,f)
                self.logger.info('Model File' + file_name+ 'saved')
                self.logger.info('End of Save Models')
                return 'Success'
        except Exception as e:
            self.logger.exception('Exception raise while saving the Model: %s' % e)
            raise Exception()

    def load_model(self,file_name):
        try:
            self.logger.info('Start of load Model')
            with open('apps/models/' + file_name + '/' + file_name + '.sav', 'rb') as f:
                self.logger.info('Model File' + file_name + 'loaded')
                self.logger.info('End of load Model')
                return pickle.load(f)
        except Exception as e:
            self.logger.exception('Exception raise while loading the Model: %s' % e)
            raise Exception()

    def correct_model(self,cluster_number):
        try:
            self.logger.info('start of finding correct Model')
            self.cluster_number = cluster_number
            self.folder_name = 'apps/models'
            self.list_of_model_files = []
            self.list_of_files = os.listdir(self.folder_name)
            for self.file in self.list_of_files:
                try:
                    if(self.file.index(str(self.cluster_number)) != -1):
                        self.model_name = self.file
                except:
                    continue
            self.model_name = self.model_name.split('.')[0]
            self.logger.info('End of finding correct model')
            return self.model_name
        except Exception as e:
            self.logger.exception('Exception raise while finding correct model: %s' % e)
            raise Exception()