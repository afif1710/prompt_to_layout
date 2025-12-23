# Docker image analysis (layers + sizes)

## Image sizes

Command:

- `docker images | findstr afif1710/aiui-`

Output:

```
C:\Users\Asus\Desktop\ai-ui-builder>docker images | findstr afif1710/aiui-
WARNING: This output is designed for human readability. For machine-readable output, please use --format.
afif1710/aiui-backend:1.0.0 995041831bb5 361MB 84.2MB U
afif1710/aiui-frontend:1.0.0 786070caa0a2 81.7MB 23.1MB U
```

## Frontend layers

Command:

- `docker history afif1710/aiui-frontend:1.0.0`

Output:

```
C:\Users\Asus\Desktop\ai-ui-builder>docker history afif1710/aiui-frontend:1.0.0
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
786070caa0a2   23 minutes ago   CMD ["nginx" "-g" "daemon off;"]                0B        buildkit.dockerfile.v0
<missing>      23 minutes ago   EXPOSE [80/tcp]                                 0B        buildkit.dockerfile.v0
<missing>      23 minutes ago   COPY /app/dist /usr/share/nginx/html # build…   393kB     buildkit.dockerfile.v0
<missing>      23 minutes ago   COPY nginx.conf /etc/nginx/conf.d/default.co…   20.5kB    buildkit.dockerfile.v0
<missing>      5 days ago       RUN /bin/sh -c set -x     && apkArch="$(cat …   43.4MB    buildkit.dockerfile.v0
<missing>      5 days ago       ENV NJS_RELEASE=1                               0B        buildkit.dockerfile.v0
<missing>      5 days ago       ENV NJS_VERSION=0.9.4                           0B        buildkit.dockerfile.v0
<missing>      5 days ago       CMD ["nginx" "-g" "daemon off;"]                0B        buildkit.dockerfile.v0
<missing>      5 days ago       STOPSIGNAL SIGQUIT                              0B        buildkit.dockerfile.v0
<missing>      5 days ago       EXPOSE map[80/tcp:{}]                           0B        buildkit.dockerfile.v0
<missing>      5 days ago       ENTRYPOINT ["/docker-entrypoint.sh"]            0B        buildkit.dockerfile.v0
<missing>      5 days ago       COPY 30-tune-worker-processes.sh /docker-ent…   16.4kB    buildkit.dockerfile.v0
<missing>      5 days ago       COPY 20-envsubst-on-templates.sh /docker-ent…   12.3kB    buildkit.dockerfile.v0
<missing>      5 days ago       COPY 15-local-resolvers.envsh /docker-entryp…   12.3kB    buildkit.dockerfile.v0
<missing>      5 days ago       COPY 10-listen-on-ipv6-by-default.sh /docker…   12.3kB    buildkit.dockerfile.v0
<missing>      5 days ago       COPY docker-entrypoint.sh / # buildkit          8.19kB    buildkit.dockerfile.v0
<missing>      5 days ago       RUN /bin/sh -c set -x     && addgroup -g 101…   5.56MB    buildkit.dockerfile.v0
<missing>      5 days ago       ENV DYNPKG_RELEASE=1                            0B        buildkit.dockerfile.v0
<missing>      5 days ago       ENV PKG_RELEASE=1                               0B        buildkit.dockerfile.v0
<missing>      5 days ago       ENV NGINX_VERSION=1.29.4                        0B        buildkit.dockerfile.v0
<missing>      5 days ago       LABEL maintainer=NGINX Docker Maintainers <d…   0B        buildkit.dockerfile.v0
<missing>      5 days ago       CMD ["/bin/sh"]                                 0B        buildkit.dockerfile.v0
<missing>      5 days ago       ADD alpine-minirootfs-3.23.2-x86_64.tar.gz /…   9.11MB    buildkit.dockerfile.v0
```

## Backend layers

Command:

- `docker history afif1710/aiui-backend:1.0.0`

Output:

```
C:\Users\Asus\Desktop\ai-ui-builder>docker history afif1710/aiui-backend:1.0.0
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
995041831bb5   11 minutes ago   CMD ["gunicorn" "--bind" "0.0.0.0:8000" "--w…   0B        buildkit.dockerfile.v0
<missing>      11 minutes ago   EXPOSE [8000/tcp]                               0B        buildkit.dockerfile.v0
<missing>      11 minutes ago   USER appuser                                    0B        buildkit.dockerfile.v0
<missing>      11 minutes ago   RUN /bin/sh -c useradd -m appuser && chown -…   365kB     buildkit.dockerfile.v0
<missing>      11 minutes ago   COPY . /app # buildkit                          299kB     buildkit.dockerfile.v0
<missing>      11 minutes ago   RUN /bin/sh -c pip install --no-cache-dir /w…   79.2MB    buildkit.dockerfile.v0
<missing>      11 minutes ago   COPY /wheels /wheels # buildkit                 14.8MB    buildkit.dockerfile.v0
<missing>      11 minutes ago   RUN /bin/sh -c apt-get update && apt-get ins…   48.2MB    buildkit.dockerfile.v0
<missing>      24 minutes ago   WORKDIR /app                                    8.19kB    buildkit.dockerfile.v0
<missing>      24 minutes ago   ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFER…   0B        buildkit.dockerfile.v0
<missing>      2 weeks ago      CMD ["python3"]                                 0B        buildkit.dockerfile.v0
<missing>      2 weeks ago      RUN /bin/sh -c set -eux;  for src in idle3 p…   16.4kB    buildkit.dockerfile.v0
<missing>      2 weeks ago      RUN /bin/sh -c set -eux;   savedAptMark="$(a…   41.3MB    buildkit.dockerfile.v0
<missing>      2 weeks ago      ENV PYTHON_SHA256=fb85a13414b028c49ba18bbd52…   0B        buildkit.dockerfile.v0
<missing>      2 weeks ago      ENV PYTHON_VERSION=3.12.12                      0B        buildkit.dockerfile.v0
<missing>      2 weeks ago      ENV GPG_KEY=7169605F62C751356D054A26A821E680…   0B        buildkit.dockerfile.v0
<missing>      2 weeks ago      RUN /bin/sh -c set -eux;  apt-get update;  a…   4.94MB    buildkit.dockerfile.v0
<missing>      2 weeks ago      ENV LANG=C.UTF-8                                0B        buildkit.dockerfile.v0
<missing>      2 weeks ago      ENV PATH=/usr/local/bin:/usr/local/sbin:/usr…   0B        buildkit.dockerfile.v0
<missing>      2 weeks ago      # debian.sh --arch 'amd64' out/ 'trixie' '@1…   87.4MB    debuerreotype 0.16
```

`````

### `docs/dockerhub-push.md` (copy the whole block)
````md
# Docker Hub push evidence

## Frontend push

Command:
- `docker compose push frontend`

Output:
`````

- Pushing afif1710/aiui-frontend:1.0.0: 33f95a0f3229 Mounted from afif1710/algosort-frontend 20.0s
- Pushing afif1710/aiui-frontend:1.0.0: 0abf9e567266 Mounted from afif1710/algosort-frontend 20.0s
- Pushing afif1710/aiui-frontend:1.0.0: 085c5e5aaa8e Mounted from afif1710/algosort-frontend 20.0s
- Pushing afif1710/aiui-frontend:1.0.0: 1074353eec0d Mounted from afif1710/algosort-frontend 20.0s
- Pushing afif1710/aiui-frontend:1.0.0: 567f84da6fbd Mounted from afif1710/algosort-frontend 20.0s
  ✔ Pushing afif1710/aiui-frontend:1.0.0: 0439f3f04782 Pushed 3.9s
- Pushing afif1710/aiui-frontend:1.0.0: de54cb821236 Mounted from afif1710/algosort-frontend 20.0s
  ✔ Pushing afif1710/aiui-frontend:1.0.0: f517ec446124 Pushed 3.7s
- Pushing afif1710/aiui-frontend:1.0.0: 25f453064fd3 Mounted from afif1710/algosort-frontend 20.0s
- Pushing afif1710/aiui-frontend:1.0.0: da7c973d8b92 Mounted from afif1710/algosort-frontend 20.0s
  ✔ Pushing afif1710/aiui-frontend:1.0.0: 0bf5b5b523c3 Pushed

```

## Backend push

Command:
- `docker compose push backend`

Output:
```

[+] Pushing 10/11
✔ Pushing afif1710/aiui-backend:1.0.0: 0486f3e21076 Layer already exists 2.7s
✔ Pushing afif1710/aiui-backend:1.0.0: 14abbc3d966a Layer already exists 2.1s

- Pushing afif1710/aiui-backend:1.0.0: dc1536126a6e Already exists 3.6s
  ✔ Pushing afif1710/aiui-backend:1.0.0: 8fbb9decbcf7 Layer already exists 2.7s
  ✔ Pushing afif1710/aiui-backend:1.0.0: d4dc512ff29c Layer already exists 2.4s
  ✔ Pushing afif1710/aiui-backend:1.0.0: 1f384a3df500 Layer already exists 2.6s
  ✔ Pushing afif1710/aiui-backend:1.0.0: 1d92352b866d Layer already exists 2.7s
  ✔ Pushing afif1710/aiui-backend:1.0.0: 1733a4cd5954 Layer already exists 2.4s
  ✔ Pushing afif1710/aiui-backend:1.0.0: dfff024aded8 Layer already exists 2.6s
  ✔ Pushing afif1710/aiui-backend:1.0.0: 89933f780550 Layer already exists 2.8s
  ✔ Pushing afif1710/aiui-backend:1.0.0: 54a3956c34d6 Layer already exists

```

```
