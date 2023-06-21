FROM python:3.11.4-bullseye AS build
ENV PYTHONDONTWRITEBYTECODE 1
# 项目目录名称
ENV project_dirname "project"

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements-build.txt
RUN python setup.py build_ext --inplace
RUN find ./${project_dirname}/ -name "__pycache__" -type d | xargs rm -rf && \
    find ./${project_dirname}/ \( -name "*.py" -o "-name" "*.c" \) -type f | xargs rm -f




FROM python:3.11.4-bullseye
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV COLUMNS=80
ENV PYTHONPATH /app
# 项目目录名称
ENV project_dirname "project"

WORKDIR /app
# 从构建阶段复制打包好的应用程序
COPY --from=build /app/${project_dirname}/ ./${project_dirname}/
COPY --from=build /app/app.py .

ENTRYPOINT ["python", "-m", "app"]
