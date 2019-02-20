FROM golang:1.6.2-onbuild

ENV KUBECTL_VERSION v1.9.11
ENV KUBECTL_SHA256 9b8d401382068f4f75441e92f281892b9513acc1df3ad8b2b187e31cb68f951a
                   
ADD https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl /bin/kubectl

RUN echo "${KUBECTL_SHA256} */bin/kubectl" | sha256sum -c - \
  && chmod ugo+x /bin/kubectl
