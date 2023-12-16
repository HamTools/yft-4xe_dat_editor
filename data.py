import struct

class YaesuFt4Xe:
    def __init__(self):
        self.__seek_pos=4698
        self.__file_path = None
        self.__channels = []

    def read(self):
        f = open(self.__file_path, 'rb')
        i=1
        while(i<160):
            f.seek(self.__seek_pos)
            channel_bytes = f.read(64)
            no=channel_bytes[0]
            is_use=channel_bytes[4]
            channel_freq,=struct.unpack('@d', channel_bytes[6:14])
            offset,=struct.unpack('@d', channel_bytes[14:22])
            channel_name=channel_bytes[42:50]
            if is_use == 1:
                self.__channels.append((no,channel_name.decode("utf-8"), channel_freq, offset, is_use))
                #print(i,'\t',channel_name.decode("utf-8"), '\t', channel_freq)
            else:
                self.__channels.append((i,'', '', '', is_use))
                #print(i,'\t','Empty')

            self.__seek_pos+=64
            i+=1
        f.close()

    def write(self, item):
        self.__seek_pos=4698
        text, col, index = item.text(), item.column(), item.row()
        f = open(self.__file_path, 'r+b')
        f.seek(self.__seek_pos+(index*64)+4)
        #use_flag = 1
        print(text)
        if(col == 2):
            print('Frequency mofify')
            print(self.__seek_pos+(index*64)+6)
            f.seek(self.__seek_pos+(index*64)+6)
            f.write(struct.pack('@d', float(text)))
        elif(col == 1):
            print('Name modify')
            print(self.__seek_pos+(index*64)+42)
            f.seek(self.__seek_pos+(index*64)+42)
            f.write(text.encode('utf-8'))
        f.close()
    def get_channels(self):
        print(self.__channels)
        return self.__channels
    def set_file_path(self, file_path):
        self.__file_path = file_path