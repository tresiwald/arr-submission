FROM base

ARG CUDA_VISIBLE_DEVICES

COPY . .

RUN pip install -r requirements.txt
RUN pip install jupyterlab
