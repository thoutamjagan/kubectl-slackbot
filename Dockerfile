FROM golang:1.10.2

ENV KUBECTL_VERSION v1.9.11
ENV KUBECTL_SHA256 3aa80b62fbd9cfa082aa26ae6a141a6ac209543d31e6f88ad5df47842ed8ddc3
                   
ADD https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl /bin/kubectl

RUN echo "${KUBECTL_SHA256} */bin/kubectl" | sha256sum -c - \
  && chmod ugo+x /bin/kubectl
