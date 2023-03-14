FROM python:bullseye

RUN pip install --upgrade pip


WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


ARG firefox_ver=93.0
ARG geckodriver_ver=0.30.0
ARG build_rev=0

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    ca-certificates apt-utils \
    && update-ca-certificates \
    \
    # Install tools for building
    && toolDeps=" \
    curl bzip2 \
    " \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    $toolDeps \
    \
    # Install dependencies for Firefox
    && apt-get install -y --no-install-recommends --no-install-suggests \
    `apt-cache depends firefox-esr | awk '/Depends:/{print$2}'` \
    # additional 'firefox-esl' dependencies which is not in 'depends' list
    libxt6 \
    \
    # Download and install Firefox
    && curl -fL -o /tmp/firefox.tar.bz2 \
    https://ftp.mozilla.org/pub/firefox/releases/${firefox_ver}/linux-x86_64/en-GB/firefox-${firefox_ver}.tar.bz2 \
    && tar -xjf /tmp/firefox.tar.bz2 -C /tmp/ \
    && mv /tmp/firefox /opt/firefox \
    \
    # Download and install geckodriver
    && curl -fL -o /tmp/geckodriver.tar.gz \
    https://github.com/mozilla/geckodriver/releases/download/v${geckodriver_ver}/geckodriver-v${geckodriver_ver}-linux64.tar.gz \
    && tar -xzf /tmp/geckodriver.tar.gz -C /tmp/ \
    && chmod +x /tmp/geckodriver \
    && mv /tmp/geckodriver /usr/local/bin/ \
    \
    # Cleanup unnecessary stuff
    && apt-get purge -y --auto-remove \
    -o APT::AutoRemove::RecommendsImportant=false \
    $toolDeps \
    && rm -rf /var/lib/apt/lists/* \
    /tmp/*



COPY . .
RUN pip install --no-cache-dir -r requirements.txt