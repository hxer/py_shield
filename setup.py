from setuptools import setup, Extension
import glob
import os
import logging
from Cython.Build import cythonize
from Cython.Compiler import Options


# 第一层的 py 文件不编译，因为 so 文件不支持直接用 python -m 来执行
# py_files = glob.glob('*/**/*.py', recursive=True)  
# setup(
#     name="python sheild",
#     version="0.1.0",
#     ext_modules=cythonize(
#         py_files,
#         nthreads=4  # 同时用 4 个进程来编译 py 到 c，根据自己的 CPU 核数来设置
#     ),
#     python_requires=">=3.11",
# )


logger = logging.getLogger("setup")

exclude_so = ["setup.py", "app.py"]
sources = ['./']
 
extensions = []
for source in sources:
    for dirpath, foldernames, filenames in os.walk(source):
        for filename in filter(lambda x: x.endswith('.py'), filenames):
            logger.debug(f"get filename: filename")
            file_path = os.path.join(dirpath, filename)
            if filename not in exclude_so:
                # file_path[:-3] 去除 .py 尾缀
                # [2:] 去除前缀 ./
                ext = file_path[:-3].replace('/', '.')[2:]
                logger.debug(f"get extension: {ext}")
                extensions.append(
                        Extension(ext, 
                                  [file_path], 
                                  extra_compile_args = ["-Os", "-g0"],
                                  extra_link_args = ["-Wl,--strip-all"]))
 
 
logger.debug("finish source file filter")
Options.docstrings = False
compiler_directives = {'optimize.unpack_method_calls': False}
setup(  
    ext_modules=cythonize(extensions, exclude=None, nthreads = 20, quiet=True, build_dir='./build',
                            language_level="3str" , compiler_directives=compiler_directives))

# run
# python setup.py build_ext --inplace -j 4