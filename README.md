# Yaesu FT-4XE dat file reader and writer
Hobby project, just for learning!<br>
<b>*The current code has not yet been tested on the device!*</b>
#### TODO's:
- TEST
- - Bin file upload to the device
- DEV
- - Refactory code
- - Extraction of all channels
- - Csv import/export implementation
- - Decrypt all binary data

## Install
- Clone the project
```bash
git clone https://github.com/HamTools/yft-4xe_dat_reader.git
```
- Cd to the project and create and activate venv
```bash
cd yft-4xe_dat_reader
python -m venv ./venv venv
source venv/bin/activate
```
- Install dependencies
```bash
pip install -r /path/to/requirements.txt
```
## Run
```bash
python main.py
```