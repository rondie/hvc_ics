FROM python:3.10.6-slim
ARG APPDIR="/home/app"
ENV PATH="${APPDIR}/.local/bin:${PATH}"
ENV HVC_ICS_UID=1000
ENV HVC_ICS_GID=1000
RUN addgroup --gid ${HVC_ICS_UID} --system app && \
    adduser --no-create-home --shell /bin/false --disabled-password --uid ${HVC_ICS_GID} --system --group app
RUN mkdir ${APPDIR} && chown -R ${HVC_ICS_UID}:${HVC_ICS_GID} ${APPDIR}
USER app
WORKDIR ${APPDIR}
COPY --chown=${HVC_ICS_UID}:${HVC_ICS_GID} requirements.txt ${APPDIR}
RUN pip3 install --no-cache-dir -r requirements.txt
COPY --chown=${HVC_ICS_UID}:${HVC_ICS_GID} . ${APPDIR}
ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "app.ics:app"]
