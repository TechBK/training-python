Training::Python
===============
`Training::Python` là bản mẫu (boilerplate) phục vụ cho công tác training Python.  
Bạn có thể tự do lựa chọn framework (Django, Flask...) cũng như bất kỳ thư viện nào cần thiết. 
Project này đơn thuần chỉ thiết lập trước một **Gialb-CI pipeline** tự động chạy *test* đồng thời *deploy* mỗi khi có commit được *push* lên `master`.

## Setup
### Setup project
* Fork this project: [dung.dm/training-python](http://git.teko.vn/dung.dm/training-python)

![Fork project](https://farm5.staticflickr.com/4238/35579204201_a5d51d0093_z.jpg)

Sau khi fork, bạn có thể đổi tên project & repo URL nếu muốn:

  1. Vào **Settings >  General**  
  2. Coi mục **Project settings** hoặc **Rename repository**

* Clone repo

```shell
$ git clone git@git.teko.vn:<username>/training-python.git
$ cd training-python
```

* Add *dung.dm*'s remote: (for keeping things up-to-date)

```shell
$ git remote add dung.dm http://git.teko.vn/dung.dm/training-python.git
```

### Setup development environment
#### Install requirements:
1. Python 3.6+
2. Pip 9+
3. virtualenv

Kiểm tra môi trường:
```shell
### Check version
$ python --version
$ python3.6 --version
$ pip --version
$ virtualenv --version

### Check install path
$ which python
$ which virtualenv
...
```

Cài đặt các packages còn thiếu như sau:
```shell
### Install Python 3.6 in Ubuntu 14.04 or 16.04
$ sudo add-apt-repository ppa:jonathonf/python-3.6
$ sudo apt update
$ sudo apt install python3.6

### Install pip
$ sudo apt install python-pip
$ pip install -U pip            # Update pip to last version

### VirtualEnv
$ sudo apt install virtualenv virtualenvwrapper
```

#### Setup VirtualEnv (Virtual Environments)
Có 2 levels có thể setup VirtualEnv:  
* [User level](#1-virtualenv-at-user-level)
* [Project level](#2-virtualenv-at-project-level)

#### 1. VirtualEnv at User level.
Nếu bạn có nhiều Python projects với môi trường giống nhau (VD: cùng Python 3.6).
Setup VirtualEnv at User level là giải pháp giúp tiết kiệm thời gian setup cho từng project.

```shell
$ virtualenv -p python3.6 $HOME
```

Thêm dòng này vào `~/.profile` hoặc `~/.bashrc` (nếu chưa có):
```shell
# set PATH so it includes user's private bin directories
PATH="$HOME/bin:$HOME/.local/bin:$PATH"
```

Kiểm tra thành quả:
```shell
$ exec -l $SHELL                # Reload shell

$ python --version
Python 3.6.1

$ pip --version
pip 9.0.1 from /home/dungdm93/lib/python3.6/site-packages (python 3.6)
```

#### 2. VirtualEnv at Project level.
Setup VirtualEnv at Project level giúp bạn cô lập (isolate) môi trường giữa các project với nhau.  
Tuy nhiên, mỗi lần trước khi thao tác trên project, bạn đều phải load lại môi trường :unamused:

```shell
$ virtualenv -p python3.6 .venv
$ source .venv/bin/activate
```

**Note**: VirtualEnv ở *Project* level sẽ override *User* level, nên bạn có thể sử dụng đồng thời cả 2 phương pháp trên. 
VD: Hầu hết project là Python 3.6 (config ở User level), song 1 số ít project sử dụng Python 2.7 (config ở Project level)

## Run & test :gear:
### Run

```shell
$ export FLASK_APP=main.py
$ flask run
```

### Test

```shell
### Unit test
$ py.test
### Pytest with coverage
$ py.test --cov=src --cov-report=term
```

### Lint: Check coding conventions

```shell
$ pip install pylint
$ pylint src
```

## Folder structure
Project này đã được config sẵn cho việc auto test & auto deploy, nên có những file bạn ko nên tự ý sửa/xóa nếu chưa hiểu rõ bản chất của nó.
* `.gitlab-ci.yml`:  
File định nghĩa pipeline, sử dụng bởi Gitlab-CI. KHÔNG nên động vào :smirk:
* `ansible/`:  
Folder chứa script deploy app lên production. Để nguyên nó đấy :sunglasses:
* `run.sh`:  
Production config VirtualEnv at Project level, tức cần load môi trường trước khi run server.
Tuy nhiên `supervisor` lại run server trong single command, do đó, `run.sh` làm nhiệm vụ wrap tất cả command đó lại.
Bạn có thể sửa nội dung nếu cần thiết.
* `var/`:  
Folder chứa các file lúc runtime, VD: log files, socket file,... git ignore tuy nhiên ko được xóa, vì sẽ gây lỗi khi chạy trên production.
* `requirements.txt`, `main.py`, folders `src/`, `tests/`:  
Bạn sửa thoải mái, song nên cần thận khi đổi tên (rename/move).  

**Important**: Contact [DungDM](https://teko.facebook.com/profile.php?id=100015907001998) để biết thêm thông tin chi tiết :cowboy:

## App Config and Database
### App Config
Trên production, app config nên được load từ file `instance/config.py`. 
File này sẽ auto-generated trong quá trình deploy dựa vào biến môi trường (`environment variables`) và template file `instance/config.py.temp`.  
Vậy để thêm một config ta cần làm 2 việc như sau:

### Define environment variables
Có một số chỗ ta có thể định nghĩa environment variables như sau:
* Secret Variables: Định nghĩa các variables cần tính bảo mật cao như password, secret keys,...  
  **Settings** > **CI/CD Pipelines** > Coi mục "**Secret Variables**"
* Global variables: Các variables sẽ share giữa các CI jobs.  
  Top-level session `variables` trong file `.gitlab-ci.yml` (Giống như `HOST_URL`)
* Job variables: Những variables chỉ xuất hiện trong job tương ứng.  
  Job-level session `variables` trong file `.gitlab-ci.yml` (Giống như `MYSQL_DATABASE` của job `test:pytest`)

### Write config.py template
// TODO

### Database
// TODO

## Others
### Get Deploy URL
Sau khi deploy xong bạn có thể tận hưởng thành quả của mình bằng cách:  
**Pipelines** > **Environments** > Click "**Open**" button bên cạnh *Environment name*.

![Get Deploy URL](https://farm5.staticflickr.com/4049/35727650805_894d01af99_z.jpg)
