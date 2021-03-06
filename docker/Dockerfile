FROM pytorch/pytorch


# apt-get
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && \
		apt-get install -y \
			build-essential curl lsof git sudo tmux tree vim wget zsh && \
		apt-get clean && \
		rm -rf /var/lib/apt/lists/* && \
		rm -rf /var/cache/apk/*


# python
ENV WORK_PATH /workspace
WORKDIR $WORK_PATH
ENV PYTHONPATH "/workspace:${PYTHONPATH}"
ENV PIP_OPTIONS "--no-cache-dir --progress-bar off"
COPY docker/requirements.txt $WORK_PATH/docker/
COPY segmentation/requirements.txt $WORK_PATH/segmentation/
RUN pip install ${PIP_OPTIONS} -r $WORK_PATH/docker/requirements.txt && \
    pip install ${PIP_OPTIONS} -r $WORK_PATH/segmentation/requirements.txt && \
		pip install ${PIP_OPTIONS} -U setuptools

# duser setting
ARG USER_ID
ARG GROUP_ID
RUN addgroup --gid $GROUP_ID duser && \
    adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID duser && \
    adduser duser sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers


# settings
USER duser
ENV SETTING_PATH /duser/settings
COPY docker/settings $SETTING_PATH
WORKDIR $SETTING_PATH
RUN $SETTING_PATH/setup.sh
SHELL ["/bin/zsh", "-c"]

# workdir
ENV SEGMENTATION_WORK_PATH $WORK_PATH/segmentation
WORKDIR $SEGMENTATION_WORK_PATH
