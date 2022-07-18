FROM continuumio/miniconda3
COPY . /home/
WORKDIR /home
RUN apt-get update
RUN apt install -y build-essential redis
RUN conda env create --file environment.yml
RUN conda init bash

ENV PATH /opt/conda/envs/bambu-server/bin:$PATH
ENV CONDA_DEFAULT_ENV bambu-server

RUN /bin/bash -c "source activate bambu-server"
RUN echo "source ~/.bashrc"
RUN echo "conda activate bambu-server" > ~/.bashrc
RUN echo "source activate bambu-server" > ~/.bashrc

SHELL ["conda", "run", "-n", "bambu-server", "/bin/bash"]
CMD ["/bin/bash", "bambu-server"]
