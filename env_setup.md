# Environment

### Create conda env
```shell
conda create -y --name=bts python=3.6.9 
```

### Remove conda env
```shell
conda env remove -y --name bts 
```

### add jupyter kernel
```shell
conda activate bts
pip install ipykernel
python -m ipykernel install --user --name bts --display-name "BTS"
```

### remove jupyter kernel
```shell
jupyter kernelspec uninstall -y bts 
```

### Fix CV2 import problem
```shell
rm /home/puff/anaconda3/envs/bts/lib/libstdc++.so.6
ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /home/puff/anaconda3/envs/bts/lib/libstdc++.so.6
```

