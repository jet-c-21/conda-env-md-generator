import argparse
import getpass

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', type=str, default='myenv')
parser.add_argument('-dn', '--display_name', type=str, default='My Env')
parser.add_argument('-pv', '--python_version', type=str, default='3.6.9')
args = parser.parse_args()
# print(f"args = {args}")

ENV_NAME = args.name
ENV_DISPLAY_NAME = args.display_name
PY_VER = args.python_version
USER = getpass.getuser()

s = \
    f"""# Environment

### Create conda env
```shell
conda create -y --name={ENV_NAME} python={PY_VER} 
```

### Remove conda env
```shell
conda env remove -y --name {ENV_NAME} 
```

### add jupyter kernel
```shell
conda activate {ENV_NAME}
pip install ipykernel
python -m ipykernel install --user --name {ENV_NAME} --display-name "{ENV_DISPLAY_NAME}"
```

### remove jupyter kernel
```shell
jupyter kernelspec uninstall -y {ENV_NAME} 
```

### Fix CV2 import problem
```shell
rm /home/{USER}/anaconda3/envs/{ENV_NAME}/lib/libstdc++.so.6
ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /home/{USER}/anaconda3/envs/{ENV_NAME}/lib/libstdc++.so.6
```

"""

print(s)

with open('env_setup.md', 'w+') as f:
    f.write(s)
