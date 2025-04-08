import configparser
import logging
import sys
import os

class Settings:
    isinstance_count = 0
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(BASE_DIR, 'config.ini'), encoding="utf-8")
        # self.config.read('config.ini',encoding='utf-8')
        self.settings()
        Settings.isinstance_count += 1
        print(f"Settings init success")

    def settings(self):
        # insert paths
        cwd = os.getcwd()
        sys.path.insert(0, cwd)

        # logging level
        log_level_str = self.config.get('Logging', 'level')
        log_level = getattr(logging, log_level_str.upper(), logging.ERROR)
        #即保存到文件，又打印到屏幕
        logging.basicConfig(level=log_level, format='%(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler("app.log"),
                                logging.StreamHandler()
                            ])
        # 打印日志级别
        log_level_name = logging.getLevelName(log_level)
        print(f'display log level: {log_level} - {log_level_name}')

            
    def __getitem__(self, keys):
        return self.config.get(keys[0], keys[1])
    
        
# Zebura settings
z_config = Settings()

# Example usage
if __name__ == '__main__':

    print("\n".join(sys.path))
    print(z_config['LLM','OPENAI_KEY'])
    message = "logging message"
    logging.debug(message)
    logging.info(message)
    logging.warning(message)
    logging.error(message)
    logging.critical(message)