HOMEPAGE_HTML = """<!DOCTYPE html>
<html lang="en-GB" class="no-js core o-typography--loading-sans o-typography--loading-sans-bold o-typography--loading-display o-typography--loading-display-bold" data-o-component="o-typography" style="overflow-x:hidden;background-color:#fff1e5;color:#33302e">
    <head>
        <meta charSet="utf-8"/>
        <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>Financial Times</title>
        <meta name="description" content="News, analysis and opinion on the latest in business, markets, economics and politics from the Financial Times, the UK&#x27;s National Newspaper of the Year 2023"/>
        <meta name="robots" content="index,follow,max-snippet:200,max-image-preview:large"/>
        <meta name="google-site-verification" content="4-t8sFaPvpO5FH_Gnw1dkM28CQepjzo8UjjAkdDflTw"/>
        <script type="application/ld+json">
            {
                "@context": "http://schema.org",
                "@type": "WebSite",
                "name": "Financial Times",
                "alternateName": "FT.com",
                "url": "http://www.ft.com"
            }</script>
        <meta property="fb:pages" content="8860325749"/>
        <meta property="twitter:site" content="@FinancialTimes"/>
        <meta name="apple-itunes-app" content="app-id=1200842933"/>
        <link rel="icon" type="image/svg+xml" href="https://www.ft.com/__origami/service/image/v2/images/raw/ftlogo-v1%3Abrand-ft-logo-square-coloured?source=update-logos&amp;format=svg"/>
        <link rel="alternate icon" type="image/png" href="https://www.ft.com/__origami/service/image/v2/images/raw/ftlogo-v1%3Abrand-ft-logo-square-coloured?source=update-logos&amp;format=png&amp;width=32&amp;height=32" sizes="32x32"/>
        <link rel="alternate icon" type="image/png" href="https://www.ft.com/__origami/service/image/v2/images/raw/ftlogo-v1%3Abrand-ft-logo-square-coloured?source=update-logos&amp;format=png&amp;width=194&amp;height=194" sizes="194x194"/>
        <link rel="apple-touch-icon" href="https://www.ft.com/__origami/service/image/v2/images/raw/ftlogo-v1%3Abrand-ft-logo-square-coloured?source=update-logos&amp;format=png&amp;width=180&amp;height=180" sizes="180x180"/>
        <link rel="manifest" href="https://www.ft.com/__assets/creatives/manifest/manifest-v6.json"/>
        <link rel="alternate" type="application/rss+xml" href="https://www.ft.com/rss/home" hrefLang="x-default"/>
        <link rel="alternate" type="application/rss+xml" href="https://www.ft.com/rss/home/uk" hrefLang="en-gb"/>
        <link rel="alternate" href="https://www.ft.com/?edition=uk" hrefLang="en-gb"/>
        <link rel="alternate" href="https://www.ft.com/?edition=international" hrefLang="x-default"/>
        <link rel="alternate" href="https://www.ft.com/" hrefLang="en-gb"/>
        <link rel="preload" as="script" href="https://static.chartbeat.com/js/chartbeat_mab.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://static.chartbeat.com/js/chartbeat.js" type="application/javascript"/>
        <script id="chartbeat-script">
            (function() {
                // Chartbeat script snippet

                function loadScript(src) {
                    const script = document.createElement('script');
                    script.async = true;
                    script.src = src;
                    script.onerror = function(error) {
                        console.warn(error)
                    }
                    ;
                    const last = document.scripts[document.scripts.length - 1];
                    last.parentNode.insertBefore(script, last);
                }

                try {

                    const testing = new URL(location).searchParams.has('chartbeatTest') || false;

                    window._sf_async_config = {
                        uid: 14181,
                        domain: testing ? 'testing.ft.com' : 'ft.com',
                        title: 'FT.com home page uk edition',
                        useCanonical: false,
                        useCanonicalDomain: false,
                        path: 'www.ft.com/?edition=uk',
                        topStorageDomain: 'ft.com',
                        loadLibrary: ()=>loadScript('https://static.chartbeat.com/js/chartbeat.js')
                    };

                    loadScript('https://static.chartbeat.com/js/chartbeat_mab.js')

                } catch (error) {
                    // clean up
                    delete window._sf_async_config
                    console.error(error)
                }
            }
            )();
        </script>
        <link href="https://cdn-pci.optimizely.com/js/22578711082.js" rel="preload" as="script" type="application/javascript"/>
        <link href="https://securepubads.g.doubleclick.net/tag/js/gpt.js" rel="preload" as="script" type="application/javascript"/>
        <script id="third-party-bootstrap-config" type="application/json">
            [
                {
                    "src": "https://cdn-pci.optimizely.com/js/22578711082.js",
                    "async": false,
                    "defer": true,
                    "always": false,
                    "enhanced": true,
                    "core": false
                },
                {
                    "src": "https://securepubads.g.doubleclick.net/tag/js/gpt.js",
                    "async": true,
                    "defer": false,
                    "always": true,
                    "enhanced": false,
                    "core": false
                }
            ]</script>
        <script>
            ;(function() {
                const isEnhanced = 'IntersectionObserver'in window && 'Promise'in window
                const scripts = getScriptsConfig()
                const status = {}
                let scriptsWaiting = 0

                if (!scripts || !scripts.length) {
                    return
                }

                scripts.filter(function(script) {
                    return script.always || (isEnhanced && script.enhanced) || (!isEnhanced && script.core)
                }).forEach(loadScript)

                function loadScript(config) {
                    try {
                        const script = document.createElement('script')
                        script.onerror = onerror(config.src)
                        script.onload = onload(config.src)
                        script.async = config.async
                        script.defer = config.defer
                        if (config.referrerPolicy) {
                            script.referrerPolicy = config.referrerPolicy
                        }
                        document.currentScript.parentNode.insertBefore(script, document.currentScript)
                        script.src = config.src
                        status[config.src] = null
                        scriptsWaiting++
                    } catch (error) {
                        console.error('Error creating script element for ' + config.src)
                        // eslint-disable-line no-console
                    }
                }

                function onload(script) {
                    return function(event) {
                        status[script] = true
                        scriptsWaiting--
                        //
                        if (!scriptsWaiting) {
                            done()
                        }
                    }
                }

                function onerror(script) {
                    return function(error) {
                        status[script] = false
                        scriptsWaiting--
                        console.error('The thirdparty script ' + script + ' failed to load')
                        // eslint-disable-line no-console
                        if (!scriptsWaiting) {
                            done()
                        }
                    }
                }

                const timer = setTimeout(done, 10000)

                function done() {
                    clearTimeout(timer)
                    try {
                        const errors = []
                        for (const key in status) {
                            if (status.hasOwnProperty(key)) {
                                if (!status[key]) {
                                    errors.push(key)
                                }
                            }
                        }
                        if (errors.length) {
                            const img = new Image()
                            const data = JSON.stringify({
                                category: 'javascript',
                                action: 'load-error',
                                system: {
                                    source: 'home-page',
                                },
                                context: {
                                    scripts: errors,
                                },
                            })

                            img.src = 'https://spoor-api.ft.com/px.gif?data=' + encodeURIComponent(data)
                        }
                    } catch (e) {
                        console.error('Problem sending error report')
                    }
                }

                function getScriptsConfig() {
                    try {
                        return JSON.parse(document.getElementById('third-party-bootstrap-config').textContent) || []
                    } catch (error) {
                        console.error('Error rehydrating third-party-bootstrap-config', error)
                        // eslint-disable-line no-console
                    }
                    return []
                }
            }
            )();
        </script>
        <script>
            !function(e, n, t, i, o, r) {
                function c(e) {
                    if ("number" != typeof e)
                        return e;
                    var n = new Date;
                    return new Date(n.getTime() + 1e3 * e)
                }
                var a = 4e3
                  , s = "xnpe_async_hide";
                function p(e) {
                    return e.reduce((function(e, n) {
                        return e[n] = function() {
                            e._.push([n.toString(), arguments])
                        }
                        ,
                        e
                    }
                    ), {
                        _: []
                    })
                }
                function m(e, n, t) {
                    var i = t.createElement(n);
                    i.src = e;
                    var o = t.getElementsByTagName(n)[0];
                    return o.parentNode.insertBefore(i, o),
                    i
                }
                function u(e) {
                    return "[object Date]" === Object.prototype.toString.call(e)
                }
                r.target = r.target,
                r.file_path = r.file_path || r.target + "/js/exponea.min.js",
                o[n] = p(["anonymize", "initialize", "identify", "update", "track", "trackLink", "trackEnhancedEcommerce", "getHtml", "showHtml", "showBanner", "showWebLayer", "ping", "getAbTest", "loadDependency", "getRecommendation", "reloadWebLayers"]),
                o[n].notifications = p(["isAvailable", "isSubscribed", "subscribe", "unsubscribe"]),
                o[n]["snippetVersion"] = "v2.3.0",
                function(e, n, t) {
                    e[n]["_" + t] = {},
                    e[n]["_" + t].nowFn = Date.now,
                    e[n]["_" + t].snippetStartTime = e[n]["_" + t].nowFn()
                }(o, n, "performance"),
                function(e, n, t, i, o, r) {
                    e[o] = {
                        sdk: e[i],
                        sdkObjectName: i,
                        skipExperiments: !!t.new_experiments,
                        sign: t.token + "/" + (r.exec(n.cookie) || ["", "new"])[1],
                        path: t.target
                    }
                }(o, e, r, n, i, RegExp("__exponea_etc__" + "=([\w-]+)")),
                function(e, n, t) {
                    m(e.file_path, n, t)
                }(r, t, e),
                function(e, n, t, i, o, r, p) {
                    if (e.new_experiments) {
                        !0 === e.new_experiments && (e.new_experiments = {});
                        var f, l = e.new_experiments.hide_class || s, _ = e.new_experiments.timeout || a, d = encodeURIComponent(r.location.href.split("#")[0]);
                        e.cookies && e.cookies.expires && ("number" == typeof e.cookies.expires || u(e.cookies.expires) ? f = c(e.cookies.expires) : e.cookies.expires.tracking && ("number" == typeof e.cookies.expires.tracking || u(e.cookies.expires.tracking)) && (f = c(e.cookies.expires.tracking))),
                        f && f < new Date && (f = void 0);
                        var x = e.target + "/webxp/" + n + "/" + r[t].sign + "/modifications.min.js?http-referer=" + d + "&timeout=" + _ + "ms" + (f ? "&cookie-expires=" + Math.floor(f.getTime() / 1e3) : "");
                        "sync" === e.new_experiments.mode && r.localStorage.getItem("__exponea__sync_modifications__") ? function(e, n, t, i, o) {
                            t[o][n] = "<" + n + ' src="' + e + '"></' + n + ">",
                            i.writeln(t[o][n]),
                            i.writeln("<" + n + ">!" + o + ".init && document.writeln(" + o + "." + n + '.replace("/' + n + '/", "/' + n + '-async/").replace("><", " async><"))</' + n + ">")
                        }(x, n, r, p, t) : function(e, n, t, i, o, r, c, a) {
                            r.documentElement.classList.add(e);
                            var s = m(t, i, r);
                            function p() {
                                o[a].init || m(t.replace("/" + i + "/", "/" + i + "-async/"), i, r)
                            }
                            function u() {
                                r.documentElement.classList.remove(e)
                            }
                            s.onload = p,
                            s.onerror = p,
                            o.setTimeout(u, n),
                            o[c]._revealPage = u
                        }(l, _, x, n, r, p, o, t)
                    }
                }(r, t, i, 0, n, o, e),
                function(e, n, t) {
                    e[n].start = function(i) {
                        i && Object.keys(i).forEach((function(e) {
                            return t[e] = i[e]
                        }
                        )),
                        e[n].initialize(t)
                    }
                }(o, n, r)
            }(document, "exponea", "script", "webxpClient", window, {
                target: 'https://bloomreach.ft.com',
                token: 'd6e5bd4c-9228-11eb-a414-9a67e462410e',
            });
        </script>
        <link rel="preconnect" href="https://spoor-api.ft.com"/>
        <link rel="preconnect" href="https://session-next.ft.com" crossorigin="use-credentials"/>
        <link rel="preconnect" href="https://ads-api.ft.com"/>
        <link rel="preconnect" href="https://securepubads.g.doubleclick.net"/>
        <link rel="preload" as="script" href="https://polyfill.io/v3/polyfill.min.js?features=default%2Ces5%2Ces2015%2Ces2016%2Ces2017%2CEventSource%2Cfetch%2CHTMLPictureElement%2CIntersectionObserver%2CNodeList.prototype.forEach&amp;source=next"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/webpack-runtime.fb5e068cad11.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/page-kit-components.90a120e9101a.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-tracking.2105c1bac798.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-n-syndication.f95eb47ab4d8.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-header.28c06e1d421d.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-viewport.23fb20fd1a89.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-n-feedback.343e703ec28a.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-grid.cdce17ebc329.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-utils.34c8411dab31.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-footer.ecd26a818094.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-message.196bbf214865.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-overlay.09ed63bf2911.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-toggle.0cf48066b7e1.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-tooltip.1d9c5f866c96.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-n-tracking.325e5447ab66.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-banner.b0af73e394f7.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-cookie-message.e95ef7281d9f.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-date.c2a540bea29c.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-o-typography.fc026638c98b.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-x-engine.1ba975d35f02.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/superstore.ffb9dad07087.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/react.8efae3892ea5.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-n-exponea.6796cd8a9092.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/financial-times-privacy-us-privacy.cbac14c27e2b.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/ftdomdelegate.28fbbd700d30.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/preact.44ad39293e48.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/shared.stable.c1624f9d9712.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/privacy-components.27db63a14d09.bundle.js" type="application/javascript"/>
        <link rel="preload" as="script" href="https://www.ft.com/__assets/hashed/page-kit/scripts.42a3cd4ef11a.bundle.js" type="application/javascript"/>
        <link rel="preload" as="font" href="https://www.ft.com/__origami/service/build/v3/font?font_format=woff2&amp;font_name=MetricWeb-Regular&amp;system_code=origami&amp;version=1.12" type="font/woff2" crossorigin="anonymous"/>
        <link rel="preload" as="font" href="https://www.ft.com/__origami/service/build/v3/font?font_format=woff2&amp;font_name=MetricWeb-Semibold&amp;system_code=origami&amp;version=1.12" type="font/woff2" crossorigin="anonymous"/>
        <link rel="preload" as="font" href="https://www.ft.com/__origami/service/build/v3/font?font_format=woff2&amp;font_name=FinancierDisplayWeb-Regular&amp;system_code=origami&amp;version=1.12" type="font/woff2" crossorigin="anonymous"/>
        <link rel="preload" as="font" href="https://www.ft.com/__origami/service/build/v3/font?font_format=woff2&amp;font_name=FinancierDisplayWeb-Bold&amp;system_code=origami&amp;version=1.12" type="font/woff2" crossorigin="anonymous"/>
        <script id="initial-props" type="application/json"></script>
        <link rel="stylesheet" href="https://www.ft.com/__assets/hashed/page-kit/vendors~page-kit-layout-styles.be49bf31d0a3.css"/>
        <link rel="stylesheet" href="https://www.ft.com/__assets/hashed/page-kit/styles.18c776959970.css"/>
        <script type="application/json" id="page-kit-bootstrap-config">
            {
                "trackErrors": true,
                "core": [
                    "https://polyfill.io/v3/polyfill.min.js?features=HTMLPictureElement&source=next"
                ],
                "enhanced": [
                    "https://polyfill.io/v3/polyfill.min.js?features=default%2Ces5%2Ces2015%2Ces2016%2Ces2017%2CEventSource%2Cfetch%2CHTMLPictureElement%2CIntersectionObserver%2CNodeList.prototype.forEach&source=next",
                    "https://www.ft.com/__assets/hashed/page-kit/webpack-runtime.fb5e068cad11.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/page-kit-components.90a120e9101a.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-tracking.2105c1bac798.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-n-syndication.f95eb47ab4d8.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-header.28c06e1d421d.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-viewport.23fb20fd1a89.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-n-feedback.343e703ec28a.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-grid.cdce17ebc329.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-utils.34c8411dab31.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-footer.ecd26a818094.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-message.196bbf214865.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-overlay.09ed63bf2911.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-toggle.0cf48066b7e1.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-tooltip.1d9c5f866c96.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-n-tracking.325e5447ab66.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-banner.b0af73e394f7.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-cookie-message.e95ef7281d9f.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-date.c2a540bea29c.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-o-typography.fc026638c98b.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-x-engine.1ba975d35f02.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/superstore.ffb9dad07087.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/react.8efae3892ea5.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-n-exponea.6796cd8a9092.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/financial-times-privacy-us-privacy.cbac14c27e2b.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/ftdomdelegate.28fbbd700d30.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/preact.44ad39293e48.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/shared.stable.c1624f9d9712.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/privacy-components.27db63a14d09.bundle.js",
                    "https://www.ft.com/__assets/hashed/page-kit/scripts.42a3cd4ef11a.bundle.js"
                ]
            }</script>
        <script>
            ;(function() {
                var doc = document.documentElement
                var isEnhanced = isEnhancedBrowser()
                var scriptsConfig = getScriptsConfig()
                var scriptsToLoad = []
                var currentScript = document.scripts[document.scripts.length - 1]

                doc.className = doc.className.replace('no-js', 'js')

                if (isEnhanced) {
                    doc.className = doc.className.replace('core', 'enhanced')
                    Array.prototype.push.apply(scriptsToLoad, scriptsConfig.enhanced)
                } else {
                    Array.prototype.push.apply(scriptsToLoad, scriptsConfig.core)
                }

                for (var i = 0, len = scriptsToLoad.length; i < len; i++) {
                    loadScript(scriptsToLoad[i])
                }

                function scriptLoadError(error) {
                    var script = error.target ? error.target.src : null

                    if (script) {
                        console.error('The script ' + script + ' failed to load')
                        // eslint-disable-line no-console
                    }

                    if (/enhanced/.test(doc.className)) {
                        console.warn('Script loading failed, reverting to core experience')
                        // eslint-disable-line no-console
                        doc.className = doc.className.replace('enhanced', 'core')
                    }

                    if (scriptsConfig.trackErrors) {
                        addErrorTrackingPixel(script)
                    }
                }

                function loadScript(src) {
                    var script = document.createElement('script')
                    script.onerror = scriptLoadError
                    script.async = false
                    script.src = src
                    currentScript.parentNode.insertBefore(script, currentScript)
                }

                // "Cut the mustard" test
                // by Maggie Allen and Matt Hinchliffe November 2018
                function isEnhancedBrowser() {
                    var script = document.createElement('script')
                    var input = document.createElement('input')

                    return ('visibilityState'in document && // not supported by old Android (4.0-4.4) without a prefix
                    'indeterminate'in input && // not supported by BB 10
                    'flex'in doc.style && // not supported by old Safari (< 9) or IE 6-10
                    'async'in script // not supported by old Opera (Presto engine < 15)
                    )
                }

                function getScriptsConfig() {
                    var scriptsConfigEl = document.getElementById('page-kit-bootstrap-config')
                    var scriptsConfig = {
                        core: [],
                        enhanced: [],
                        trackErrors: false
                    }

                    if (scriptsConfigEl) {
                        try {
                            scriptsConfig = JSON.parse(scriptsConfigEl.innerHTML)
                        } catch (error) {
                            console.error('Bootstrap configuration error', error)
                            // eslint-disable-line no-console
                        }
                    }

                    return scriptsConfig
                }

                function addErrorTrackingPixel(script) {
                    var img = new Image()

                    var data = JSON.stringify({
                        category: 'javascript',
                        action: 'load-error',
                        system: {
                            source: 'page-kit'
                        },
                        context: {
                            script: script
                        }
                    })

                    img.src = 'https://spoor-api.ft.com/px.gif?data=' + encodeURIComponent(data)
                }
            }
            )()
        </script>
        <script>
            (function(w, d, s, l, i) {
                w[l] = w[l] || [];
                w[l].push({
                    'gtm.start': new Date().getTime(),
                    event: 'gtm.js'
                });
                var f = d.getElementsByTagName(s)[0]
                  , j = d.createElement(s)
                  , dl = l != 'dataLayer' ? '&l=' + l : '';
                j.async = true;
                j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
                f.parentNode.insertBefore(j, f);
            }
            )(window, document, 'script', 'dataLayer', 'GTM-NWQJW68');
        </script>
        <script>
            (function loadCustomFonts() {
                var rootElement = document.documentElement;
                if (/(^|\s)o-typography-fonts-loaded=1(;|$)/.test(document.cookie)) {
                    var fontLabels = ['sans', 'sans-bold', 'display', 'display-bold'];
                    for (var i = 0; i < fontLabels.length; i++) {
                        rootElement.className = rootElement.className.replace('o-typography--loading-' + fontLabels[i], '');
                    }
                }
            }());
        </script>
    </head>
    <body>
        <noscript>
            <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NWQJW68" height="0" width="0" style="display:none;visibility:hidden"></iframe>
        </noscript>
        <div class="n-layout">
            <a data-trackable="a11y-skip-to-help" class="n-layout__skip-link" href="https://www.ft.com/accessibility">Accessibility help</a>
            <a data-trackable="a11y-skip-to-navigation" class="n-layout__skip-link" href="#site-navigation">Skip to navigation</a>
            <a data-trackable="a11y-skip-to-content" class="n-layout__skip-link" href="#site-content">Skip to content</a>
            <a data-trackable="a11y-skip-to-footer" class="n-layout__skip-link" href="#site-footer">Skip to footer</a>
            <div class="n-layout__row n-layout__row--header">
                <div class="n-layout__header-before">
                    <pg-slot data-config-key="top-desktop"></pg-slot>
                    <div class="markets-data-wrapper js-markets-data">
                        <div class="o-grid-container">
                            <div class="markets-data" data-trackable="header | markets data">
                                <ul class="markets-data__items markets-data__items--hidden"></ul>
                                <a href="https://markets.ft.com/data" class="markets-data__item-link" data-trackable="link">Visit Markets Data</a>
                            </div>
                        </div>
                    </div>
                    <div id="n-exponea-bottom-slot"></div>
                    <div>
                        <div class="n-messaging-slot" data-n-messaging-slot="bottom" data-n-messaging-name="cookieConsentC" data-trackable="onsite-message-cookieConsentC" data-n-messaging-tooltip="">
                            <div data-o-component="o-cookie-message" class="o-cookie-message " role="dialog" aria-labelledby="cookie-banner-aria-label" aria-describedby="cookie-banner-aria-description">
                                <div class="o-cookie-message__outer" data-nosnippet>
                                    <div class="o-cookie-message__inner">
                                        <div class="o-cookie-message__content">
                                            <div class="o-cookie-message__heading">
                                                <h2 id="cookie-banner-aria-label">Cookies on FT Sites</h2>
                                            </div>
                                            <p id="cookie-banner-aria-description">
                                                We use
								<a href="https://help.ft.com/help/legal-privacy/cookies/" class="o-cookie-message__link o-cookie-message__link--external" target="_blank" rel="noopener" data-n-messaging-policy>cookies</a>
                                                and other data for a number of reasons, such as keeping FT Sites reliable and secure,
								personalising content and ads, providing social media features and to
								analyse how our Sites are used.
							
                                            </p>
                                        </div>
                                        <div class="o-cookie-message__actions">
                                            <div class="o-cookie-message__action">
                                                <a data-n-messaging-accept-cookies href="https://consent.ft.com/__consent/consent-record-cookie?redirect=https://www.ft.com" class="o-cookie-message__button">Accept cookies
								</a>
                                            </div>
                                            <div class="o-cookie-message__action o-cookie-message__action--secondary">
                                                <a data-n-messaging-manage-cookies href="/preferences/manage-cookies" class="o-cookie-message__link">Manage cookies
								</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <header id="site-navigation" class="o-header o-header--large-logo" data-o-component="o-header" data-o-header--no-js="true" tabindex="-1">
                    <div class="o-header__row o-header__anon" data-trackable="header-anon">
                        <ul class="o-header__anon-list">
                            <li class="o-header__anon-item">
                                <a class="o-header__anon-link" href="/login?location=/" data-trackable="Sign In">Sign In</a>
                            </li>
                            <li class="o-header__anon-item">
                                <a class="o-header__anon-link" href="/products?segmentId=f860e6c2-18af-ab30-cd5e-6e3a456f9265" data-trackable="Subscribe">Subscribe</a>
                            </li>
                        </ul>
                    </div>
                    <div class="o-header__row o-header__top" data-trackable="header-top">
                        <div class="o-header__container">
                            <div class="o-header__top-wrapper">
                                <div class="o-header__top-column o-header__top-column--left">
                                    <a href="#o-header-drawer" class="o-header__top-icon-link o-header__top-icon-link--menu" aria-controls="o-header-drawer" title="Open side navigation menu" data-trackable="drawer-toggle">
                                        <span class="o-header__top-link-label">Open side navigation menu</span>
                                    </a>
                                    <a href="#o-header-search-primary" class="o-header__top-icon-link o-header__top-icon-link--search" aria-controls="o-header-search-primary" title="Open search bar" data-trackable="search-toggle">
                                        <span class="o-header__top-link-label">Open search bar</span>
                                    </a>
                                </div>
                                <div class="o-header__top-column o-header__top-column--center">
                                    <a class="o-header__top-logo" style="background-image:none" data-trackable="logo" href="/" title="Go to Financial Times homepage">
                                        <svg viewBox="0 0 1054 86">
                                            <title>Financial Times</title>
                                            <path d="M26.177 72.609c0 5.938 1.697 7.295 12.554 7.295v3.732H.9v-3.732c7.464 0 10.01-.679 10.01-7.125V12.215c0-6.447-2.546-7.126-10.01-7.126V1.357h63.448l.34 22.563h-3.054C59.937 6.956 55.696 5.43 39.919 5.43H26.008v33.59h11.196c10.688 0 11.367-1.697 12.215-10.179h3.054v24.599h-3.054c-.848-8.482-1.527-10.01-12.215-10.01H26.008v29.18h.17zm46.314 11.027v-3.732c7.465 0 10.01-.679 10.01-7.125V12.215c0-6.447-2.545-7.126-10.01-7.126V1.357h35.287V5.09c-7.465 0-10.01.679-10.01 7.126v60.564c0 6.446 2.545 7.125 10.01 7.125v3.732H72.49zm115.36 1.357l-56.323-69.725V72.44c0 6.617 4.58 7.634 12.385 7.634v3.733h-29.858v-3.733c7.803 0 12.045-1.017 12.045-7.634V8.991c-3.563-3.732-6.108-3.902-12.045-3.902V1.357h26.465l43.09 55.475V12.554c0-6.616-4.58-7.634-12.384-7.634V1.357h30.027V5.09c-7.803 0-12.045 1.018-12.045 7.635v72.27h-1.357zm40.207-1.357h-29.689v-3.732c7.804 0 11.367-1.018 13.911-7.804L239.085.509h7.464l28.84 72.1c2.545 6.447 3.732 7.125 9.67 7.125v3.732h-34.438v-3.732c10.518 0 11.536-.848 8.99-7.125l-8.481-21.884h-25.787L217.71 71.93c-2.375 6.447 1.357 7.804 10.518 7.804v3.902h-.17zm-1.188-37.153h22.393l-11.705-29.518-10.688 29.518zm135.548 38.51l-56.153-69.725V72.44c0 6.617 4.58 7.634 12.384 7.634v3.733h-29.18v-3.733c7.126 0 11.367-1.017 11.367-7.634V9.161c-4.071-3.732-7.125-4.072-13.91-4.072V1.357h28.16l43.09 55.475V12.554c0-6.616-4.58-7.634-12.383-7.634V1.357h29.858V5.09c-7.804 0-12.045 1.018-12.045 7.635v72.27h-1.188zm83.297-83.805h2.036l1.187 24.598-3.053.17c-2.036-14.08-9.5-21.545-23.242-21.545-15.268 0-26.804 13.063-26.804 33.081 0 25.617 16.116 40.206 33.08 40.206 7.296 0 13.912-2.035 20.358-8.99l2.376 2.374c-5.26 7.465-15.608 13.742-29.52 13.742-20.696 0-41.732-15.608-41.732-41.734C380.4 17.813 399.57 0 422.813 0c11.027 0 16.795 4.75 19.848 4.75 1.357 0 2.375-1.187 3.054-3.562zm12.723 82.448v-3.732c7.465 0 10.01-.679 10.01-7.125V12.215c0-6.447-2.545-7.126-10.01-7.126V1.357h35.287V5.09c-7.464 0-10.01.679-10.01 7.126v60.564c0 6.446 2.546 7.125 10.01 7.125v3.732h-35.287zm68.538 0h-27.653v-3.732c6.108 0 9.331-1.018 11.876-7.804L538.003.509h7.464l28.84 72.1c2.545 6.447 3.733 7.125 9.67 7.125v3.732H549.54v-3.732c10.518 0 11.536-.848 8.991-7.125l-8.482-21.884h-25.786l-7.635 21.205c-2.375 6.447 1.358 7.804 10.519 7.804v3.902h-.17zm-1.188-37.153h22.394l-11.536-29.518-10.858 29.518zm63.957 37.153v-3.732c7.465 0 10.01-.679 10.01-7.125V12.215c0-6.447-2.545-7.126-10.01-7.126V1.357h35.117V5.09c-7.464 0-9.84.679-9.84 7.126v61.073c0 5.428 2.715 6.107 7.126 6.107h4.241c15.947 0 21.036-2.375 25.447-20.527l3.054.339-2.545 24.26h-62.6v.17zM760.75 1.357l.339 23.92h-3.054C756.34 7.634 752.098 5.43 736.32 5.43h-5.089v67.18c0 6.447 2.375 7.295 12.554 7.295v3.732h-40.376v-3.732c10.179 0 12.723-1.018 12.723-7.295V5.429h-5.089c-15.777 0-20.018 2.205-21.715 19.848h-3.053l.339-23.92h74.136zm7.973 82.28v-3.733c7.465 0 10.01-.679 10.01-7.125V12.215c0-6.447-2.545-7.126-10.01-7.126V1.357h35.287V5.09c-7.465 0-10.01.679-10.01 7.126v60.564c0 6.446 2.545 7.125 10.01 7.125v3.732h-35.287zM910.21 1.356V5.09c-7.465 0-10.688.34-10.01 6.956l6.447 61.073c.679 6.277 3.054 6.955 10.518 6.955v3.733h-35.117v-3.733c7.295 0 9.84-.678 9.331-6.955L884.762 8.99l-25.956 76.172h-1.018L832.34 8.822l-6.108 64.126c-.678 6.447 3.733 7.125 11.197 7.125v3.733h-27.483v-3.733c7.465 0 10.01-1.187 10.518-7.125l6.447-61.073c.679-6.446-2.545-6.955-10.01-6.955V1.357h28.84l17.305 56.153 18.661-56.153h28.5zm65.653 52.082h-3.053c-.849-8.482-1.527-10.01-12.215-10.01H948.04v29.859c0 5.428 2.715 6.107 7.125 6.107h6.786c15.947 0 21.036-2.375 25.447-20.527l3.054.339-2.884 24.26h-64.805v-3.733c7.464 0 10.009-.678 10.009-7.125V12.215c0-6.447-2.545-7.126-10.01-7.126V1.357h62.261l.34 20.527h-3.054c-1.866-14.59-5.598-16.286-21.885-16.286H948.21v33.42h12.554c10.687 0 11.366-1.696 12.214-10.178h3.054v24.599h-.17zm65.484 13.232c0-7.464-4.75-11.196-12.893-15.777l-13.063-6.786c-9.84-5.259-15.607-11.027-15.607-21.375C999.783 9.84 1010.81 0 1025.23 0c9.84 0 14.929 4.75 17.813 4.75 1.866 0 2.714-1.187 3.562-3.562h2.375l1.188 23.072-3.054.17c-1.696-11.198-9.67-19.85-20.866-19.85-8.483 0-14.081 5.09-14.081 12.215 0 7.804 5.937 11.027 12.554 14.59l11.196 5.937c10.519 5.768 17.983 11.536 17.983 22.563 0 14.59-12.554 24.939-28.161 24.939-11.028 0-16.456-5.26-19.34-5.26-1.866 0-2.884 1.697-3.732 4.242h-2.376l-1.696-24.43 3.054-.339c2.375 15.268 12.893 21.545 23.411 21.545 8.822-.17 16.286-4.071 16.286-13.91z" fill="#231F20" fill-rule="evenodd"></path>
                                        </svg>
                                    </a>
                                </div>
                                <div class="o-header__top-column o-header__top-column--right">
                                    <a class="o-header__top-button o-header__top-button--hide-m" role="button" href="/products?segmentId=f860e6c2-18af-ab30-cd5e-6e3a456f9265" data-trackable="Subscribe">Subscribe</a>
                                    <a class="o-header__top-link o-header__top-link--hide-m" href="/login?location=/" data-trackable="Sign In">Sign In</a>
                                    <a class="o-header__top-icon-link o-header__top-icon-link--myft o-header__top-icon-link--show-m" id="o-header-top-link-myft" href="/myft" data-trackable="my-ft" data-tour-stage="myFt" aria-label="My F T">
                                        <span class="o-header__visually-hidden">myFT</span>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div id="o-header-search-primary" class="o-header__row o-header__search o-header__search--primary" data-trackable="header-search" data-o-header-search="true">
                        <div class="o-header__container">
                            <form class="o-header__search-form" action="/search" role="search" aria-label="Site search" data-n-topic-search="true" data-n-topic-search-categories="concepts,equities" data-n-topic-search-view-all="true">
                                <label class="o-header__visually-hidden" for="o-header-search-term-primary">
                                    Search the <abbr title="Financial Times">FT</abbr>
                                </label>
                                <input type="text" class="o-header__search-term" id="o-header-search-term-primary" name="q" autoComplete="off" autoCorrect="off" autoCapitalize="off" spellcheck="false" data-trackable="search-term" placeholder="Search the FT" data-n-topic-search-input="true"/>
                                <button class="o-header__search-submit" type="submit" data-trackable="search-submit">Search</button>
                                <button class="o-header__search-close o--if-js" type="button" aria-controls="o-header-search-primary" title="Close search bar" data-trackable="close">
                                    <span class="o-header__visually-hidden">Close search bar</span>
                                </button>
                            </form>
                        </div>
                    </div>
                    <nav id="o-header-nav-mobile" class="o-header__row o-header__nav o-header__nav--mobile" aria-hidden="true" data-trackable="header-nav:mobile">
                        <ul class="o-header__nav-list">
                            <li class="o-header__nav-item">
                                <a class="o-header__nav-link o-header__nav-link--primary" href="/" aria-label="Home, current page" aria-current="page" data-trackable="Home">Home</a>
                            </li>
                            <li class="o-header__nav-item">
                                <a class="o-header__nav-link o-header__nav-link--primary" href="https://markets.ft.com/data" data-trackable="Markets Data">Markets Data</a>
                            </li>
                        </ul>
                    </nav>
                    <nav id="o-header-nav-desktop" class="o-header__row o-header__nav o-header__nav--desktop" role="navigation" aria-label="Primary navigation" data-trackable="header-nav:desktop">
                        <div class="o-header__container">
                            <ul class="o-header__nav-list o-header__nav-list--left" data-trackable="primary-nav">
                                <li class="o-header__nav-item">
                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/" id="o-header-link-0" aria-label="Home, current page" aria-current="page" data-trackable="Home">Home</a>
                                </li>
                                <li class="o-header__nav-item">
                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/world" id="o-header-link-1" data-trackable="World">World</a>
                                    <div class="o-header__mega" id="o-header-mega-1" role="group" aria-labelledby="o-header-link-1" data-o-header-mega="true" data-trackable="meganav | World">
                                        <div class="o-header__container">
                                            <div class="o-header__mega-wrapper">
                                                <div class="o-header__mega-column o-header__mega-column--subsections" data-trackable="sections">
                                                    <div class="o-header__mega-heading">Sections</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/world" data-trackable="link">World Home</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/israel-hamas-war" data-trackable="link">Israel-Hamas war</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/global-economy" data-trackable="link">Global Economy</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/world-uk" data-trackable="link">UK</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/us" data-trackable="link">US</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/china" data-trackable="link">China</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/africa" data-trackable="link">Africa</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/asia-pacific" data-trackable="link">Asia Pacific</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/emerging-markets" data-trackable="link">Emerging Markets</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/europe" data-trackable="link">Europe</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/war-in-ukraine" data-trackable="link">War in Ukraine</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/americas" data-trackable="link">Americas</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/middle-east-north-africa" data-trackable="link">Middle East &amp;North Africa</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="o-header__mega-column o-header__mega-column--articles" data-trackable="popular">
                                                    <div class="o-header__mega-heading">Most Read</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/312e43f2-a8be-445d-9d46-88d2ddf174a7" data-trackable="link">Far-right leader Geert Wilders wins most votes in Dutch election</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/56f7d6d6-6a93-4172-a49e-d8a91991e29d" data-trackable="link">US thwarted plot to kill Sikh separatist on American soil</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/ed4b352b-5c06-4f8d-9df7-1b1f9fecb269" data-trackable="link">Donald Trump would gut Joe Biden’s landmark IRA climate law if elected</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/81717934-e941-4064-9371-30c517399879" data-trackable="link">Military briefing: has Israel achieved its war aims in Gaza?</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/60674329-5be3-4802-a05a-851ee2990efd" data-trackable="link">How Germany’s ‘debt brake’ broke the budget</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                                <li class="o-header__nav-item">
                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/world-uk" id="o-header-link-2" data-trackable="UK">UK</a>
                                    <div class="o-header__mega" id="o-header-mega-2" role="group" aria-labelledby="o-header-link-2" data-o-header-mega="true" data-trackable="meganav | UK">
                                        <div class="o-header__container">
                                            <div class="o-header__mega-wrapper">
                                                <div class="o-header__mega-column o-header__mega-column--subsections" data-trackable="sections">
                                                    <div class="o-header__mega-heading">Sections</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/world-uk" data-trackable="link">UK Home</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/uk-economy" data-trackable="link">UK Economy</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/uk-politics" data-trackable="link">UK Politics</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/brexit" data-trackable="link">Brexit</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/uk-companies" data-trackable="link">UK Companies</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/personal-finance" data-trackable="link">Personal Finance</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="o-header__mega-column o-header__mega-column--articles" data-trackable="popular">
                                                    <div class="o-header__mega-heading">Most Read</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/cae9b213-e793-4d4c-8025-b6573e70fd0f" data-trackable="link">Jeremy Hunt cuts national insurance but taxes head to postwar high</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/9ac523da-1c15-43e8-9ccc-bbfdbce4b74a" data-trackable="link">Sunak under pressure as net migration to UK hits record 745,000 </a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/3f4f0e67-2825-492a-897d-0691fbb24a27" data-trackable="link">Hunt may be lucky but he has not solved the UK growth challenge</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/0d9269ac-bd22-40fa-8d14-b1b6590edb96" data-trackable="link">Jeremy Hunt to offer UK workers ‘pot for life’ in sweeping pension reforms</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/2314fb09-7f58-45e1-86ab-4767e9139ad3" data-trackable="link">British tech tycoon Lawrence Jones guilty of rape and sexual assault</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                                <li class="o-header__nav-item">
                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/companies" id="o-header-link-3" data-trackable="Companies">Companies</a>
                                    <div class="o-header__mega" id="o-header-mega-3" role="group" aria-labelledby="o-header-link-3" data-o-header-mega="true" data-trackable="meganav | Companies">
                                        <div class="o-header__container">
                                            <div class="o-header__mega-wrapper">
                                                <div class="o-header__mega-column o-header__mega-column--subsections" data-trackable="sections">
                                                    <div class="o-header__mega-heading">Sections</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/companies" data-trackable="link">Companies Home</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/energy" data-trackable="link">Energy</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/financials" data-trackable="link">Financials</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/health" data-trackable="link">Health</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/industrials" data-trackable="link">Industrials</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/media" data-trackable="link">Media</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/professional-services" data-trackable="link">Professional Services</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/retail-consumer" data-trackable="link">Retail &amp;Consumer</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/technology-sector" data-trackable="link">Tech Sector</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/telecoms" data-trackable="link">Telecoms</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/transport" data-trackable="link">Transport</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="o-header__mega-column o-header__mega-column--articles" data-trackable="popular">
                                                    <div class="o-header__mega-heading">Most Read</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/fa41fb97-9f1f-4351-ac03-c5e1a2e50ebe" data-trackable="link">Toyota advert banned for showing pick-up truck convoy driving through river  </a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/4f46e278-971e-49f0-ab05-47b3a57997ec" data-trackable="link">Chinese shadow bank Zhongzhi faces $36bn shortfall after ‘management ran wild’</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/7caceb97-c7cf-40be-93ea-4b8ac9919bf7" data-trackable="link">UBS chief Sergio Ermotti calls for tougher sanctions on negligent bankers</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/c00073c1-22c3-40b7-923f-a3cbf71875f2" data-trackable="link">Bayer drug setback adds to new CEO’s problems  </a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/f9197565-4c71-402f-a609-cb5d8c6e7a79" data-trackable="link">Pret A Manger owner JAB names new chief as Olivier Goudet steps down</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                                <li class="o-header__nav-item">
                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/technology" id="o-header-link-4" data-trackable="Tech">Tech</a>
                                </li>
                                <li class="o-header__nav-item">
                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/markets" id="o-header-link-5" data-trackable="Markets">Markets</a>
                                    <div class="o-header__mega" id="o-header-mega-5" role="group" aria-labelledby="o-header-link-5" data-o-header-mega="true" data-trackable="meganav | Markets">
                                        <div class="o-header__container">
                                            <div class="o-header__mega-wrapper">
                                                <div class="o-header__mega-column o-header__mega-column--subsections" data-trackable="sections">
                                                    <div class="o-header__mega-heading">Sections</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/markets" data-trackable="link">Markets Home</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/alphaville" data-trackable="link">Alphaville</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="https://markets.ft.com/data" data-trackable="link">Markets Data</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/cryptofinance" data-trackable="link">Cryptofinance</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/capital-markets" data-trackable="link">Capital Markets</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/commodities" data-trackable="link">Commodities</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/currencies" data-trackable="link">Currencies</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/equities" data-trackable="link">Equities</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/fund-management" data-trackable="link">Fund Management</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/ft-wealth-management" data-trackable="link">Wealth Management</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/ft-trading-room" data-trackable="link">Trading</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/moral-money" data-trackable="link">Moral Money</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="https://etf.ft.com" data-trackable="link">ETF Hub</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="o-header__mega-column o-header__mega-column--articles" data-trackable="popular">
                                                    <div class="o-header__mega-heading">Most Read</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/d713ae81-0652-4bca-b71f-4943cf5b870a" data-trackable="link">Live news: European stocks close higher after positive economic data</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/17f49c0b-9792-4db5-9592-ffff22fbc941" data-trackable="link">Anglo American’s high-stakes bet on a new way to feed the world</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/7caceb97-c7cf-40be-93ea-4b8ac9919bf7" data-trackable="link">UBS chief Sergio Ermotti calls for tougher sanctions on negligent bankers</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/dddd51c4-7c5b-4488-b935-6099788bbc89" data-trackable="link">Hedge fund short sellers suffer $43bn of losses in market rally</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/fe528c26-a39c-4488-bbb7-5feaa5ed3b54" data-trackable="link">Binance’s crypto dominance under threat after loss of founder Changpeng Zhao</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                                <li class="o-header__nav-item">
                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/climate-capital" id="o-header-link-6" data-trackable="Climate">Climate</a>
                                </li>
                                <li class="o-header__nav-item">
                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/opinion" id="o-header-link-7" data-trackable="Opinion">Opinion</a>
                                    <div class="o-header__mega" id="o-header-mega-7" role="group" aria-labelledby="o-header-link-7" data-o-header-mega="true" data-trackable="meganav | Opinion">
                                        <div class="o-header__container">
                                            <div class="o-header__mega-wrapper">
                                                <div class="o-header__mega-column o-header__mega-column--subsections" data-trackable="sections">
                                                    <div class="o-header__mega-heading">Sections</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/opinion" data-trackable="link">Opinion Home</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/columnists" data-trackable="link">Columnists</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/ft-view" data-trackable="link">The FT View</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/lex" data-trackable="link">Lex</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/obituaries" data-trackable="link">Obituaries</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/letters" data-trackable="link">Letters</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="o-header__mega-column o-header__mega-column--articles" data-trackable="popular">
                                                    <div class="o-header__mega-heading">Most Read</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/a9ea4937-6a02-4eed-b751-adaca5076d84" data-trackable="link">A Tory chancellor walks into a bar . . . </a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/78a5a870-3243-480f-a532-f5066f590e13" data-trackable="link">There is a crisis of confidence in Israel and Zionism</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/8279eb63-395a-4ff2-99c3-250409e03941" data-trackable="link">OpenAI has just fused its corporate ‘kill switch’</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/8c23c566-cb73-4983-9773-b20917bc323f" data-trackable="link">What if US income inequality has not risen?</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/c88634cd-ea99-41ec-8422-b47ed2ffc45a" data-trackable="link">There is a scientific fraud epidemic — and we are ignoring the cure</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                                <li class="o-header__nav-item">
                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/work-careers" id="o-header-link-8" data-trackable="Work &amp; Careers">Work &amp;Careers</a>
                                    <div class="o-header__mega" id="o-header-mega-8" role="group" aria-labelledby="o-header-link-8" data-o-header-mega="true" data-trackable="meganav | Work &amp; Careers">
                                        <div class="o-header__container">
                                            <div class="o-header__mega-wrapper">
                                                <div class="o-header__mega-column o-header__mega-column--subsections" data-trackable="sections">
                                                    <div class="o-header__mega-heading">Sections</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/work-careers" data-trackable="link">Work &amp;Careers Home</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="https://rankings.ft.com/" data-trackable="link">Business School Rankings</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/business-education" data-trackable="link">Business Education</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/entrepreneurship" data-trackable="link">Entrepreneurship</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/recruitment" data-trackable="link">Recruitment</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/business-books" data-trackable="link">Business Books</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/business-travel" data-trackable="link">Business Travel</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/working-it" data-trackable="link">Working It</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="o-header__mega-column o-header__mega-column--articles" data-trackable="popular">
                                                    <div class="o-header__mega-heading">Most Read</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/6ee16212-c748-44df-8698-b646f722deb7" data-trackable="link">Brexit negotiator Michel Barnier: ‘The EU is not the same one the UK left’</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/c42006d9-f3c6-4b5a-a42d-f32f7be9915c" data-trackable="link">In search of chief executives who never grow ‘old’</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/7944d5a5-5933-4d0c-a45d-078dde7c986b" data-trackable="link">The inescapable tyranny of the bad boss</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/0eb7cb51-6ccb-4277-b457-a0ad86c2ba68" data-trackable="link">Business Books: What to read this month</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/562f1c34-c1c3-400f-8d93-f6f5fa0bcce9" data-trackable="link">Start-ups challenge culture of the Japanese salaryman</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                                <li class="o-header__nav-item">
                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/life-arts" id="o-header-link-9" data-trackable="Life &amp; Arts">Life &amp;Arts</a>
                                    <div class="o-header__mega" id="o-header-mega-9" role="group" aria-labelledby="o-header-link-9" data-o-header-mega="true" data-trackable="meganav | Life &amp; Arts">
                                        <div class="o-header__container">
                                            <div class="o-header__mega-wrapper">
                                                <div class="o-header__mega-column o-header__mega-column--subsections" data-trackable="sections">
                                                    <div class="o-header__mega-heading">Sections</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/life-arts" data-trackable="link">Life &amp;Arts Home</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/arts" data-trackable="link">Arts</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/books" data-trackable="link">Books</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/food-drink" data-trackable="link">Food &amp;Drink</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/magazine" data-trackable="link">FT Magazine</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/house-home" data-trackable="link">House &amp;Home</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/style" data-trackable="link">Style</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/travel" data-trackable="link">Travel</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/globetrotter" data-trackable="link">FT Globetrotter</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="o-header__mega-column o-header__mega-column--articles" data-trackable="popular">
                                                    <div class="o-header__mega-heading">Most Read</div>
                                                    <div class="o-header__mega-content">
                                                        <ul class="o-header__mega-list">
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/74240f9f-f09c-4b15-9011-dccbea2e000c" data-trackable="link">Leon Black’s downfall confounds the legacy of #MeToo on Wall Street</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/b12fbaa3-150d-4e46-bad7-25d0f79b03a7" data-trackable="link">Luxury fashion prices have gone too far</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/d46b742b-b906-4c51-8468-112798cc8ee4" data-trackable="link">The downsizer’s dilemma: how the property market is trapping would-be movers</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/2b0c050f-f776-4292-8ce7-884beceef4be" data-trackable="link">Ukraine: the new fissures in a society under strain</a>
                                                            </li>
                                                            <li class="o-header__mega-item">
                                                                <a class="o-header__mega-link" href="/content/f892799e-8749-49f4-bba3-30188559af80" data-trackable="link">Theorising only gets you so far in bed </a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                                <li class="o-header__nav-item">
                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/htsi" id="o-header-link-10" data-trackable="HTSI">HTSI</a>
                                </li>
                            </ul>
                        </div>
                    </nav>
                </header>
                <header class="o-header o-header--simple o-header--sticky o--if-js" data-o-component="o-header" data-o-header--sticky="true" aria-hidden="true">
                    <div class="o-header__row o-header__top" data-trackable="header-sticky">
                        <div class="o-header__container">
                            <div class="o-header__top-wrapper">
                                <div class="o-header__top-column o-header__top-column--left">
                                    <a href="#" class="o-header__top-icon-link o-header__top-icon-link--menu" aria-controls="o-header-drawer" data-trackable="drawer-toggle" tabindex="-1">
                                        <span class="o-header__top-link-label">Menu</span>
                                    </a>
                                    <a href="#" class="o-header__top-icon-link o-header__top-icon-link--search" aria-controls="o-header-search-sticky" data-trackable="search-toggle" tabindex="-1">
                                        <span class="o-header__top-link-label">Search</span>
                                    </a>
                                </div>
                                <div class="o-header__top-column o-header__top-column--center">
                                    <div class="o-header__top-takeover">
                                        <div class="o-header__nav">
                                            <ul class="o-header__nav-list o-header__nav-list--left" data-trackable="primary-nav">
                                                <li class="o-header__nav-item">
                                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/" data-trackable="Home" tabindex="-1">Home</a>
                                                </li>
                                                <li class="o-header__nav-item">
                                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/world" data-trackable="World" tabindex="-1">World</a>
                                                </li>
                                                <li class="o-header__nav-item">
                                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/world-uk" data-trackable="UK" tabindex="-1">UK</a>
                                                </li>
                                                <li class="o-header__nav-item">
                                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/companies" data-trackable="Companies" tabindex="-1">Companies</a>
                                                </li>
                                                <li class="o-header__nav-item">
                                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/technology" data-trackable="Tech" tabindex="-1">Tech</a>
                                                </li>
                                                <li class="o-header__nav-item">
                                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/markets" data-trackable="Markets" tabindex="-1">Markets</a>
                                                </li>
                                                <li class="o-header__nav-item">
                                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/climate-capital" data-trackable="Climate" tabindex="-1">Climate</a>
                                                </li>
                                                <li class="o-header__nav-item">
                                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/opinion" data-trackable="Opinion" tabindex="-1">Opinion</a>
                                                </li>
                                                <li class="o-header__nav-item">
                                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/work-careers" data-trackable="Work &amp; Careers" tabindex="-1">Work &amp;Careers</a>
                                                </li>
                                                <li class="o-header__nav-item">
                                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/life-arts" data-trackable="Life &amp; Arts" tabindex="-1">Life &amp;Arts</a>
                                                </li>
                                                <li class="o-header__nav-item">
                                                    <a class="o-header__nav-link o-header__nav-link--primary" href="/htsi" data-trackable="HTSI" tabindex="-1">HTSI</a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                    <a class="o-header__top-logo o-header__hide--L" data-trackable="logo" href="/" title="Go to Financial Times homepage" tabindex="-1">
                                        <span class="o-header__visually-hidden">Financial Times</span>
                                    </a>
                                </div>
                                <div class="o-header__top-column o-header__top-column--right">
                                    <div class="o-header__nav">
                                        <div class="o-header__top-column o-header__top-column--right">
                                            <a class="o-header__top-button o-header__top-button--hide-m" role="button" href="/products?segmentId=f860e6c2-18af-ab30-cd5e-6e3a456f9265" data-trackable="Subscribe" tabindex="-1">Subscribe</a>
                                            <a class="o-header__top-link " href="/login?location=/" data-trackable="Sign In" tabindex="-1">Sign In</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div id="o-header-search-sticky" class="o-header__row o-header__search o-header__search--sticky" data-trackable="header-search" data-o-header-search="true">
                        <div class="o-header__container">
                            <form class="o-header__search-form" action="/search" role="search" aria-label="Site search" data-n-topic-search="true" data-n-topic-search-categories="concepts,equities" data-n-topic-search-view-all="true">
                                <label class="o-header__visually-hidden" for="o-header-search-term-sticky">
                                    Search the <abbr title="Financial Times">FT</abbr>
                                </label>
                                <input type="text" class="o-header__search-term" id="o-header-search-term-sticky" name="q" autoComplete="off" autoCorrect="off" autoCapitalize="off" spellcheck="false" data-trackable="search-term" placeholder="Search the FT" data-n-topic-search-input="true"/>
                                <button class="o-header__search-submit" type="submit" data-trackable="search-submit">Search</button>
                                <button class="o-header__search-close o--if-js" type="button" aria-controls="o-header-search-sticky" title="Close search bar" data-trackable="close">
                                    <span class="o-header__visually-hidden">Close search bar</span>
                                </button>
                            </form>
                        </div>
                    </div>
                </header>
            </div>
            <div class="n-layout__row n-layout__row--content">
                <div>
                    <h1 class="o-normalise-visually-hidden">Financial Times Home</h1>
                    <div id="n-exponea-top-slot"></div>
                    <div></div>
                    <main id="site-content">
                        <div data-trackable="list:top-stories;listTitle:empty" data-trackable-context-list-type="top-stories" data-trackable-context-list-position="0" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice story-group-named-slice top-stories-slice slice__no-title slice--default">
                                <div class="slice__content">
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span4 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:uk-immigration;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="uk-immigration" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="3" class="layout-desktop--full-height">
                                                    <div class="story-group-stacked">
                                                        <div class="story-group-stacked__primary-story">
                                                            <div class="story-group__article story-group__article--lead">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="3" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                    <div class="grid-item grid-item--span-3">
                                                                        <div class="grid grid--1-columns grid--s3-spacing">
                                                                            <div class="primary-story__teaser">
                                                                                <div class="story-group__title">
                                                                                    <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/uk-immigration" class="link" target="_self" aria-hidden="false">
                                                                                        <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">UK immigration</span>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="headline js-teaser-headline headline--scale-7 headline--color-black" data-content-id="9ac523da-1c15-43e8-9ccc-bbfdbce4b74a" data-is-exclusive="false" data-is-scoop="false">
                                                                                    <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/9ac523da-1c15-43e8-9ccc-bbfdbce4b74a" class="link" target="_self" aria-hidden="false">
                                                                                        <span class="text text--color-black text-display--scale-7 text--weight-500" id="">Sunak under pressure as net migration to UK hits record 745,000 </span>
                                                                                    </a>
                                                                                </div>
                                                                                <p class="standfirst">
                                                                                    <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/9ac523da-1c15-43e8-9ccc-bbfdbce4b74a" class="link" target="_self" aria-hidden="false">
                                                                                        <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Figures for 2022 cause alarm within Conservative party but ONS signals levels may be coming down</span>
                                                                                    </a>
                                                                                </p>
                                                                            </div>
                                                                            <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                <div class="metadata metadata__timestamp">
                                                                                    <div class="timestamp timestamp--updated">
                                                                                        <span class="timestamp-prefix">updated  </span>
                                                                                        <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T17:33:22+0000"></time>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="grid grid--1-columns grid__story-group-wrapper--secondary" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="stacked-secondary-story stacked-secondary-story--span-1 stacked-secondary-story--col-1 stacked-secondary-story--row-grid-1 stacked-secondary-story--row-stack-2">
                                                                <div class="separator--solid"></div>
                                                                <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="3" class="grid grid--1-columns grid--s3-spacing">
                                                                    <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="7f52662c-6a27-4541-84f9-0a97157fedc8" data-is-exclusive="false" data-is-scoop="false">
                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/7f52662c-6a27-4541-84f9-0a97157fedc8" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Home Office looks at ways to cut legal migration to UK</span>
                                                                        </a>
                                                                    </div>
                                                                    <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                        <div class="metadata metadata__timestamp"></div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="stacked-secondary-story stacked-secondary-story--span-1 stacked-secondary-story--col-1 stacked-secondary-story--row-grid-2 stacked-secondary-story--row-stack-3">
                                                                <div class="separator--solid"></div>
                                                                <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="2" data-trackable-context-story-siblings="3" class="grid grid--1-columns grid--s3-spacing">
                                                                    <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="e1cabc36-d050-4674-a16c-fff60c548174" data-is-exclusive="false" data-is-scoop="false">
                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/e1cabc36-d050-4674-a16c-fff60c548174" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Migration to rich countries hits all-time high </span>
                                                                        </a>
                                                                    </div>
                                                                    <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                        <div class="metadata metadata__timestamp"></div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span6 layout-desktop__grid--column-start-5 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:mining;storyGroup:medium" data-trackable-context-storygroup-size="medium" data-trackable-context-storygroup-title="mining" data-trackable-context-storygroup-position="1" data-trackable-context-storygroup-siblings="3" class="layout-desktop--full-height">
                                                    <div class="story-group story-group--featured">
                                                        <div class="grid grid--2-columns grid--fullHeight" style="grid-template-rows:auto;-ms-grid-rows:auto">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-2 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--featured">
                                                                    <div data-trackable="story:featured" data-trackable-context-story-type="featured" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="featured-story featured-story--theme-tinted">
                                                                        <div class="featured-story__image">
                                                                            <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/17f49c0b-9792-4db5-9592-ffff22fbc941" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F3d4f5fad-d7b7-4eac-aace-f48a22bb0b6c.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F3d4f5fad-d7b7-4eac-aace-f48a22bb0b6c.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F3d4f5fad-d7b7-4eac-aace-f48a22bb0b6c.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down" alt="Anglo American’s high-stakes bet on a new way to feed the world" class="image image--width-580"/>
                                                                                </picture>
                                                                            </a>
                                                                        </div>
                                                                        <div class="featured-story-content">
                                                                            <div class="story-group__title">
                                                                                <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/mining" class="link" target="_self" aria-hidden="false">
                                                                                    <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Mining</span>
                                                                                </a>
                                                                            </div>
                                                                            <div class="headline js-teaser-headline headline--scale-5 headline--color-black" data-content-id="17f49c0b-9792-4db5-9592-ffff22fbc941" data-is-exclusive="false" data-is-scoop="false">
                                                                                <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/17f49c0b-9792-4db5-9592-ffff22fbc941" class="link" target="_self" aria-hidden="false">
                                                                                    <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                        <span class="text text--color-black text-display--scale-5 text--weight-600" id="">The Big Read. </span>
                                                                                    </span>
                                                                                    <span class="text text--color-black text-display--scale-5 text--weight-400" id="">Anglo American’s high-stakes bet on a new way to feed the world</span>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span2 layout-desktop__grid--column-start-11 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:editor-s-picks;storyGroup:xsmall" data-trackable-context-storygroup-size="xsmall" data-trackable-context-storygroup-title="editor-s-picks" data-trackable-context-storygroup-position="2" data-trackable-context-storygroup-siblings="3" class="layout-desktop--full-height">
                                                    <div class="story-group story-group--extra-small">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-0 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="2" class="grid grid--1-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-1">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <span class="text text--color-claret text-sans--scale-0 text--weight-400" id="">Editor &#x27;s picks</span>
                                                                                    </div>
                                                                                    <div class="primary-story__image primary-story__image--1-cols">
                                                                                        <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/10599688-464a-4a7b-83ca-8510aec8edc2" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                            <picture>
                                                                                                <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F30f8d8d6-3930-43f1-875b-10e4b4d41b79.jpg?source=next-home-page&amp;dpr=2&amp;width=180&amp;fit=scale-down"/>
                                                                                                <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F30f8d8d6-3930-43f1-875b-10e4b4d41b79.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                                <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F30f8d8d6-3930-43f1-875b-10e4b4d41b79.jpg?source=next-home-page&amp;dpr=2&amp;width=180&amp;fit=scale-down" alt="Crypto power struggle enters new stage with Binance settlement" class="image image--width-180"/>
                                                                                            </picture>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="10599688-464a-4a7b-83ca-8510aec8edc2" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/10599688-464a-4a7b-83ca-8510aec8edc2" class="link" target="_self" aria-hidden="false">
                                                                                            <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                                <span class="icon icon--opinion icon--scale-3">
                                                                                                    <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                                </span>
                                                                                            </span>
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Crypto power struggle enters new stage with Binance settlement</span>
                                                                                        </a>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__opinion">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Ffthead-v1_gillian-tett-0df947ec-cd61-4d74-b2d8-e5f832415f1a.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Ffthead-v1_gillian-tett-0df947ec-cd61-4d74-b2d8-e5f832415f1a.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Ffthead-v1_gillian-tett-0df947ec-cd61-4d74-b2d8-e5f832415f1a.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi" alt="" class="image image--width-40"/>
                                                                                        </picture>
                                                                                        <div class="author-opinion-details">
                                                                                            <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/gillian-tett" class="link" target="_self" aria-hidden="false">
                                                                                                <span class="text text--color-black text-sans--scale-0" id="">Gillian Tett</span>
                                                                                            </a>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1 story-group--full-width-0 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="2" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="8279eb63-395a-4ff2-99c3-250409e03941" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/8279eb63-395a-4ff2-99c3-250409e03941" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="icon icon--opinion icon--scale-3">
                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                    </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-3 text--weight-500" id="">OpenAI has just fused its corporate ‘kill switch’</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__opinion">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FJohn-Thornhill-cb9e3fe5-a71d-446c-8af6-22909f40f5c3.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FJohn-Thornhill-cb9e3fe5-a71d-446c-8af6-22909f40f5c3.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FJohn-Thornhill-cb9e3fe5-a71d-446c-8af6-22909f40f5c3.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi" alt="" class="image image--width-40"/>
                                                                                </picture>
                                                                                <div class="author-opinion-details">
                                                                                    <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/john-thornhill" class="link" target="_self" aria-hidden="false">
                                                                                        <span class="text text--color-black text-sans--scale-0" id="">John Thornhill</span>
                                                                                    </a>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <section class="slice advert-slice slice__no-title">
                            <div class="slice__content">
                                <div class="layout-tablet__grid-container">
                                    <div class="layout-tablet__grid layout-tablet__grid--span12 layout-tablet__grid--column-start-1 layout-tablet__grid--row-start-1">
                                        <div class="layout__grid-content">
                                            <pg-slot data-config-key="high-impact"></pg-slot>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <div data-trackable="list:top-stories;listTitle:top-stories" data-trackable-context-list-type="top-stories" data-trackable-context-list-position="2" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice top-stories-slice slice--default">
                                <div class="slice__content">
                                    <div class="separator--dotted"></div>
                                    <header id="top-stories" class="slice-heading">
                                        <h2 class="slice-heading__title">
                                            <span class="text text--color-black-80 text-sans--scale-0" id="">Top stories</span>
                                        </h2>
                                    </header>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:lawrence-jones;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="lawrence-jones" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/2314fb09-7f58-45e1-86ab-4767e9139ad3" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F60936964-23d1-4b78-96e8-37b54a4579c6.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F60936964-23d1-4b78-96e8-37b54a4579c6.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F60936964-23d1-4b78-96e8-37b54a4579c6.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="British tech tycoon Lawrence Jones guilty of rape and sexual assault" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/stream/57afc2ba-73ba-42da-8433-0ad6ae1e9d05" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Lawrence Jones</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="2314fb09-7f58-45e1-86ab-4767e9139ad3" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/2314fb09-7f58-45e1-86ab-4767e9139ad3" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">British tech tycoon Lawrence Jones guilty of rape and sexual assault</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/2314fb09-7f58-45e1-86ab-4767e9139ad3" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Founder of web hosting business UKFast convicted of attacking three women</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp">
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T14:30:09+0000">3 hours ago</time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-4 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:uk-tax;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="uk-tax" data-trackable-context-storygroup-position="1" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="2" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/1be81df1-8d75-4a43-8da0-a9735a3e88ee" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fde68a8d4-492e-483e-b3ff-bc8594b0030d.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fde68a8d4-492e-483e-b3ff-bc8594b0030d.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fde68a8d4-492e-483e-b3ff-bc8594b0030d.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="UK households to be £1,900 poorer by 2025, think-tank says" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/uk-tax" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">UK tax</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="1be81df1-8d75-4a43-8da0-a9735a3e88ee" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/1be81df1-8d75-4a43-8da0-a9735a3e88ee" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">UK households to be £1,900 poorer by 2025, think-tank says</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/1be81df1-8d75-4a43-8da0-a9735a3e88ee" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Resolution Foundation’s findings lay bare parlous state of living standards underlying Autumn Statement</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp">
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T15:56:06+0000">2 hours ago</time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="2" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="8db41ac4-16d4-406d-b02c-5108c680af6e" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/8db41ac4-16d4-406d-b02c-5108c680af6e" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Jeremy Hunt defends tax cuts despite pressure on public services</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-7 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:tesla-inc;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="tesla-inc" data-trackable-context-storygroup-position="2" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/31ac4ef0-e945-4a9f-acb7-8330ab35680e" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fbfecab8c-af67-46c9-a3db-ae56d86d4ade.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fbfecab8c-af67-46c9-a3db-ae56d86d4ade.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fbfecab8c-af67-46c9-a3db-ae56d86d4ade.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="Tesla strikes in Sweden are ‘insane’, says Elon Musk" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/stream/35edec46-ef7b-4f9b-b85a-25174e6e07fa" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Tesla Inc</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="31ac4ef0-e945-4a9f-acb7-8330ab35680e" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/31ac4ef0-e945-4a9f-acb7-8330ab35680e" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Tesla strikes in Sweden are ‘insane’, says Elon Musk</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/31ac4ef0-e945-4a9f-acb7-8330ab35680e" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Industrial action at carmaker over collective bargaining sparks wave of sympathy strikes that could spill into other countries </span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp timestamp--new">
                                                                                            <span class="timestamp-prefix">new  </span>
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T17:52:02+0000"></time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-10 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:israel-hamas-war;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="israel-hamas-war" data-trackable-context-storygroup-position="3" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="2" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/8a08dcfc-0822-40d7-bc53-a7d079799c2c" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F29e4c1b3-11d4-429c-91ef-3b27ffbce287.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F29e4c1b3-11d4-429c-91ef-3b27ffbce287.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F29e4c1b3-11d4-429c-91ef-3b27ffbce287.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="Israel-Hamas truce and hostage deal to start Friday, says Qatar" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/israel-hamas-war" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Israel-Hamas war</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="8a08dcfc-0822-40d7-bc53-a7d079799c2c" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/8a08dcfc-0822-40d7-bc53-a7d079799c2c" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Israel-Hamas truce and hostage deal to start Friday, says Qatar</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/8a08dcfc-0822-40d7-bc53-a7d079799c2c" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Some captives held in Gaza to be freed in exchange for a four-day truce and release of Palestinian prisoners</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp">
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T15:37:42+0000">2 hours ago</time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="2" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="7171b1ba-ffbb-4d5a-a61f-9df53162fd10" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/7171b1ba-ffbb-4d5a-a61f-9df53162fd10" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                    </span>
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">The FT View. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">A much-needed truce between Israel and Hamas</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata">
                                                                                <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/ft-view" class="link" target="_self" aria-hidden="false">
                                                                                    <span class="text text--color-black text-sans--scale-0" id="">The editorial board</span>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <section class="slice advert-slice slice__no-title">
                            <div class="slice__content">
                                <div class="layout-tablet__grid-container">
                                    <div class="layout-tablet__grid layout-tablet__grid--span12 layout-tablet__grid--column-start-1 layout-tablet__grid--row-start-1">
                                        <div class="layout__grid-content">
                                            <pg-slot data-config-key="mid-desktop"></pg-slot>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <section class="slice advert-slice slice__no-title">
                            <div class="slice__content">
                                <div class="layout-tablet__grid-container">
                                    <div class="layout-tablet__grid layout-tablet__grid--span12 layout-tablet__grid--column-start-1 layout-tablet__grid--row-start-1">
                                        <div class="layout__grid-content">
                                            <pg-slot data-config-key="top-mobile"></pg-slot>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <div data-trackable="list:top-stories;listTitle:spotlight" data-trackable-context-list-type="top-stories" data-trackable-context-list-position="5" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice top-stories-slice slice--default">
                                <div class="slice__content">
                                    <div class="separator--dotted"></div>
                                    <header id="spotlight" class="slice-heading">
                                        <h2 class="slice-heading__title">
                                            <span class="text text--color-black-80 text-sans--scale-0" id="">Spotlight</span>
                                        </h2>
                                    </header>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span12 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:spotlight;storyGroup:xlarge" data-trackable-context-storygroup-size="xlarge" data-trackable-context-storygroup-title="spotlight" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="1" class="layout-desktop--full-height">
                                                    <div class="spotlight-story spotlight-story--theme-default">
                                                        <div class="grid grid--12-columns grid--fullHeight">
                                                            <div class="spotlight-grid--primary-story">
                                                                <div>
                                                                    <div data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="2" class="grid grid--10-columns grid--fullHeight">
                                                                        <div class="spotlight-story-main__wrapper">
                                                                            <div class="spotlight-story-main__teaser">
                                                                                <div class="headline js-teaser-headline headline--scale-5 headline--color-black" data-content-id="81717934-e941-4064-9371-30c517399879" data-is-exclusive="false" data-is-scoop="false">
                                                                                    <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/81717934-e941-4064-9371-30c517399879" class="link" target="_self" aria-hidden="false">
                                                                                        <span class="text text--color-black text-display--scale-5 text--weight-400" id="">Military briefing: has Israel achieved its war aims in Gaza?</span>
                                                                                    </a>
                                                                                </div>
                                                                                <p class="standfirst">
                                                                                    <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/81717934-e941-4064-9371-30c517399879" class="link" target="_self" aria-hidden="false">
                                                                                        <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Benjamin Netanyahu remains a long way from his objectives despite the deal to free some of the hostages taken by Hamas</span>
                                                                                    </a>
                                                                                </p>
                                                                            </div>
                                                                            <div class="grid-item grid-item--span-3 grid-item--align-self-end">
                                                                                <div class="metadata metadata__timestamp"></div>
                                                                            </div>
                                                                        </div>
                                                                        <div class="spotlight-story-main__image">
                                                                            <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/81717934-e941-4064-9371-30c517399879" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F03328892-e226-45e7-a53c-4abca63ac3f8.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F03328892-e226-45e7-a53c-4abca63ac3f8.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F03328892-e226-45e7-a53c-4abca63ac3f8.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down" alt="Military briefing: has Israel achieved its war aims in Gaza?" class="image image--width-580"/>
                                                                                </picture>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="spotlight-grid--secondary-story">
                                                                <div class="separator--solid"></div>
                                                                <div data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="2" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                    <div class="grid-item grid-item--span-3">
                                                                        <div class="grid grid--1-columns grid--s3-spacing">
                                                                            <div class="primary-story__image primary-story__image--1-cols">
                                                                                <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/2b0c050f-f776-4292-8ce7-884beceef4be" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                    <picture>
                                                                                        <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F094b3e0b-0663-4383-8b36-ef99ee19e72a.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                        <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F094b3e0b-0663-4383-8b36-ef99ee19e72a.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                        <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F094b3e0b-0663-4383-8b36-ef99ee19e72a.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="Ukraine: the new fissures in a society under strain" class="image image--width-280"/>
                                                                                    </picture>
                                                                                </a>
                                                                            </div>
                                                                            <div class="primary-story__teaser">
                                                                                <div class="story-group__title">
                                                                                    <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/war-in-ukraine" class="link" target="_self" aria-hidden="false">
                                                                                        <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">War in Ukraine</span>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="2b0c050f-f776-4292-8ce7-884beceef4be" data-is-exclusive="false" data-is-scoop="false">
                                                                                    <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/2b0c050f-f776-4292-8ce7-884beceef4be" class="link" target="_self" aria-hidden="false">
                                                                                        <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-600" id="">FT Magazine. </span>
                                                                                        </span>
                                                                                        <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Ukraine: the new fissures in a society under strain</span>
                                                                                    </a>
                                                                                </div>
                                                                                <p class="standfirst">
                                                                                    <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/2b0c050f-f776-4292-8ce7-884beceef4be" class="link" target="_self" aria-hidden="false">
                                                                                        <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">For all their stoical resistance Ukrainians are increasingly riven between those who stayed and those who left, those who fought and those who didn’t </span>
                                                                                    </a>
                                                                                </p>
                                                                            </div>
                                                                            <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                <div class="metadata metadata__timestamp"></div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <section class="slice advert-slice slice__no-title">
                            <div class="slice__content">
                                <div class="layout-tablet__grid-container">
                                    <div class="layout-tablet__grid layout-tablet__grid--span12 layout-tablet__grid--column-start-1 layout-tablet__grid--row-start-1">
                                        <div class="layout__grid-content">
                                            <pg-slot data-config-key="mid-mobile"></pg-slot>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <div data-trackable="list:top-stories;listTitle:news" data-trackable-context-list-type="top-stories" data-trackable-context-list-position="7" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice top-stories-slice slice--default">
                                <div class="slice__content">
                                    <div class="separator--dotted"></div>
                                    <header id="news" class="slice-heading">
                                        <h2 class="slice-heading__title">
                                            <span class="text text--color-black-80 text-sans--scale-0" id="">News</span>
                                        </h2>
                                    </header>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:dutch-election;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="dutch-election" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="2" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/e7b7b93f-166f-4043-a1c4-a6943693f33e" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F063f75e3-a081-4c69-a37e-b3b14ef08014.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F063f75e3-a081-4c69-a37e-b3b14ef08014.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F063f75e3-a081-4c69-a37e-b3b14ef08014.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="Wilders’ win in Dutch election is a boon for Europe’s far right" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/dutch-election" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Dutch election</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="e7b7b93f-166f-4043-a1c4-a6943693f33e" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/e7b7b93f-166f-4043-a1c4-a6943693f33e" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Wilders’ win in Dutch election is a boon for Europe’s far right</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/e7b7b93f-166f-4043-a1c4-a6943693f33e" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Veteran anti-Islam, anti-EU politician has capitalised on voter fears about immigration</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp">
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T16:53:22+0000">1 hour ago</time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="2" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="fb6a8318-d2c7-449c-8114-26cae3ec6941" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/fb6a8318-d2c7-449c-8114-26cae3ec6941" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                    </span>
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Instant Insight. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Far-right Dutch victory puts European liberal democracy on defensive</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__opinion">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Ffthead-v1_tony-barber-2e1beae7-a1d0-48ce-b770-0b16f32e534e.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Ffthead-v1_tony-barber-2e1beae7-a1d0-48ce-b770-0b16f32e534e.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Ffthead-v1_tony-barber-2e1beae7-a1d0-48ce-b770-0b16f32e534e.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi" alt="" class="image image--width-40"/>
                                                                                </picture>
                                                                                <div class="author-opinion-details">
                                                                                    <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/tony-barber" class="link" target="_self" aria-hidden="false">
                                                                                        <span class="text text--color-black text-sans--scale-0" id="">Tony Barber</span>
                                                                                    </a>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-4 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:sexual-misconduct-allegations;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="sexual-misconduct-allegations" data-trackable-context-storygroup-position="1" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/8c1aa6a0-d2c5-4073-b9ad-2dece3724ae2" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fded2437b-d8fa-4384-81a7-204bb2b574c2.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fded2437b-d8fa-4384-81a7-204bb2b574c2.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fded2437b-d8fa-4384-81a7-204bb2b574c2.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="New York law unleashes ‘avalanche’ of historic sexual abuse claims" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/sexual-misconduct-allegations" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Sexual misconduct allegations</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="8c1aa6a0-d2c5-4073-b9ad-2dece3724ae2" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/8c1aa6a0-d2c5-4073-b9ad-2dece3724ae2" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">New York law unleashes ‘avalanche’ of historic sexual abuse claims</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/8c1aa6a0-d2c5-4073-b9ad-2dece3724ae2" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Almost 3,000 lawsuits have been filed in the year since the Adult Survivors Act passed</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp"></div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-7 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:german-economy;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="german-economy" data-trackable-context-storygroup-position="2" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="2" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/c0d9c754-a9c0-415c-bdaf-03af3bf191aa" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F68e77cba-1056-4db4-a6eb-eed91c29dd17.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F68e77cba-1056-4db4-a6eb-eed91c29dd17.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F68e77cba-1056-4db4-a6eb-eed91c29dd17.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="Germany to suspend borrowing limits for fourth year after debt brake ruling" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/german-economy" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">German economy</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="c0d9c754-a9c0-415c-bdaf-03af3bf191aa" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/c0d9c754-a9c0-415c-bdaf-03af3bf191aa" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Germany to suspend borrowing limits for fourth year after debt brake ruling</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/c0d9c754-a9c0-415c-bdaf-03af3bf191aa" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Berlin to ask parliament to declare ‘exceptional emergency’ allowing it to create supplementary 2023 budget</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp timestamp--new">
                                                                                            <span class="timestamp-prefix">new  </span>
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T17:32:52+0000"></time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="2" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="60674329-5be3-4802-a05a-851ee2990efd" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/60674329-5be3-4802-a05a-851ee2990efd" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">How Germany’s ‘debt brake’ broke the budget</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp">
                                                                                <div class="timestamp">
                                                                                    <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T16:38:28+0000">1 hour ago</time>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-10 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:most-read;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="most-read" data-trackable-context-storygroup-position="3" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="list list--vertical">
                                                        <h2 class="list__title">Most read</h2>
                                                        <ol class="list__items-wrapper">
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="0" data-trackable-context-story-siblings="5" data-id="most-read-id" data-name="list" data-type="list" data-subtype="most-read" class="list__item">
                                                                    <div class="list__item-link">
                                                                        <div class="headline js-teaser-headline headline--scale-0 headline--color-black" data-content-id="312e43f2-a8be-445d-9d46-88d2ddf174a7" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/312e43f2-a8be-445d-9d46-88d2ddf174a7" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-0 text--weight-500" id="">Far-right’s Geert Wilders wins big in Dutch election</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="1" data-trackable-context-story-siblings="5" data-id="most-read-id" data-name="list" data-type="list" data-subtype="most-read" class="list__item">
                                                                    <div class="list__item-link">
                                                                        <div class="headline js-teaser-headline headline--scale-0 headline--color-black" data-content-id="ed4b352b-5c06-4f8d-9df7-1b1f9fecb269" data-is-exclusive="false" data-is-scoop="true">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/ed4b352b-5c06-4f8d-9df7-1b1f9fecb269" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-0 text--weight-500" id="">Trump would gut Biden’s landmark IRA climate law if elected</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="2" data-trackable-context-story-siblings="5" data-id="most-read-id" data-name="list" data-type="list" data-subtype="most-read" class="list__item list__item--pointcut">
                                                                    <div class="list__item-link">
                                                                        <div class="headline js-teaser-headline headline--scale-0 headline--color-black" data-content-id="4f46e278-971e-49f0-ab05-47b3a57997ec" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/4f46e278-971e-49f0-ab05-47b3a57997ec" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-0 text--weight-500" id="">Chinese shadow bank Zhongzhi faces $36bn shortfall after ‘management ran wild’</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="3" data-trackable-context-story-siblings="5" data-id="most-read-id" data-name="list" data-type="list" data-subtype="most-read" class="list__item">
                                                                    <div class="list__item-link">
                                                                        <div class="headline js-teaser-headline headline--scale-0 headline--color-black" data-content-id="9ac523da-1c15-43e8-9ccc-bbfdbce4b74a" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/9ac523da-1c15-43e8-9ccc-bbfdbce4b74a" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-0 text--weight-500" id="">Sunak under pressure as net migration to UK hits record 745,000 </span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="4" data-trackable-context-story-siblings="5" data-id="most-read-id" data-name="list" data-type="list" data-subtype="most-read" class="list__item">
                                                                    <div class="list__item-link">
                                                                        <div class="headline js-teaser-headline headline--scale-0 headline--color-black" data-content-id="cae9b213-e793-4d4c-8025-b6573e70fd0f" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/cae9b213-e793-4d4c-8025-b6573e70fd0f" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-0 text--weight-500" id="">Hunt cuts national insurance but taxes head to postwar high</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                        </ol>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <div data-trackable="list:top-stories;listTitle:empty" data-trackable-context-list-type="top-stories" data-trackable-context-list-position="8" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice top-stories-slice slice__no-title slice--default">
                                <div class="slice__content">
                                    <div class="separator--solid"></div>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:wilkinson-hardware-stores;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="wilkinson-hardware-stores" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/1d4df990-b62d-448c-9aa9-d5a7e17371e4" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F134bfc94-76dd-4e21-8cc8-ad37c902c083.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F134bfc94-76dd-4e21-8cc8-ad37c902c083.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F134bfc94-76dd-4e21-8cc8-ad37c902c083.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="Wilko bosses and auditor to be quizzed by MPs over retailer’s collapse  " class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/stream/a8b0bf4d-3bbf-4f75-a030-e87c4912e072" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Wilkinson Hardware Stores</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="1d4df990-b62d-448c-9aa9-d5a7e17371e4" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/1d4df990-b62d-448c-9aa9-d5a7e17371e4" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Wilko bosses and auditor to be quizzed by MPs over retailer’s collapse  </span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/1d4df990-b62d-448c-9aa9-d5a7e17371e4" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Former CEO and chair of discount chain and EY representatives will face questions </span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp timestamp--new">
                                                                                            <span class="timestamp-prefix">new  </span>
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T17:51:19+0000"></time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-4 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:tci-fund-management;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="tci-fund-management" data-trackable-context-storygroup-position="1" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/2130bef3-e34a-43cf-a224-1f56c6ab5940" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe6440e4a-0353-45f5-ac07-380169497b1c.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe6440e4a-0353-45f5-ac07-380169497b1c.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe6440e4a-0353-45f5-ac07-380169497b1c.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="TCI joins hedge fund race to open UAE office" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/stream/3c69dc90-f894-4e2d-bf82-ac52b503125c" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">TCI Fund Management</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="2130bef3-e34a-43cf-a224-1f56c6ab5940" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/2130bef3-e34a-43cf-a224-1f56c6ab5940" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">TCI joins hedge fund race to open UAE office</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/2130bef3-e34a-43cf-a224-1f56c6ab5940" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Christopher Hohn sets up Abu Dhabi base as group expands beyond traditional financial hubs of London and New York</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp">
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T15:45:08+0000">2 hours ago</time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-7 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:greek-politics;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="greek-politics" data-trackable-context-storygroup-position="2" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/46f692e9-3753-4740-b3ad-37d4693b40d9" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe348fe88-1a16-4563-b48b-5d7a0fea8af6.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe348fe88-1a16-4563-b48b-5d7a0fea8af6.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe348fe88-1a16-4563-b48b-5d7a0fea8af6.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="Greek leftist Syriza party suffers wave of resignations " class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/greek-politics" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Greek politics</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="46f692e9-3753-4740-b3ad-37d4693b40d9" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/46f692e9-3753-4740-b3ad-37d4693b40d9" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Greek leftist Syriza party suffers wave of resignations </span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/46f692e9-3753-4740-b3ad-37d4693b40d9" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Departures signal possible break-up of party that led the country during the euro crisis</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp timestamp--new">
                                                                                            <span class="timestamp-prefix">new  </span>
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T17:18:08+0000"></time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-10 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:indian-politics-and-policy;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="indian-politics-and-policy" data-trackable-context-storygroup-position="3" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="2" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/66809c9a-1a0d-4e88-adbf-5b2baece6aac" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F54cd6d57-7b53-44f9-a277-787be666f1d2.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F54cd6d57-7b53-44f9-a277-787be666f1d2.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F54cd6d57-7b53-44f9-a277-787be666f1d2.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="Alleged plot to assassinate Sikh separatist complicates US-India ties" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/indian-politics-policy" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Indian politics &amp;policy</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="66809c9a-1a0d-4e88-adbf-5b2baece6aac" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/66809c9a-1a0d-4e88-adbf-5b2baece6aac" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Alleged plot to assassinate Sikh separatist complicates US-India ties</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/66809c9a-1a0d-4e88-adbf-5b2baece6aac" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Concerns of New Delhi involvement in attempted killing on US soil come as Washington has been seeking closer relations </span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp">
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T16:19:07+0000">1 hour ago</time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="2" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="56f7d6d6-6a93-4172-a49e-d8a91991e29d" data-is-exclusive="false" data-is-scoop="true">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/56f7d6d6-6a93-4172-a49e-d8a91991e29d" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">US thwarted plot to kill Sikh separatist on American soil</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <div data-trackable="list:top-stories;listTitle:empty" data-trackable-context-list-type="top-stories" data-trackable-context-list-position="9" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice top-stories-slice slice__no-title slice--default">
                                <div class="slice__content">
                                    <div class="separator--solid"></div>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:us-presidential-election-2024;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="us-presidential-election-2024" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/ed4b352b-5c06-4f8d-9df7-1b1f9fecb269" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fb32a722f-d400-4fbd-9f0e-3f51a5c39ee7.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fb32a722f-d400-4fbd-9f0e-3f51a5c39ee7.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fb32a722f-d400-4fbd-9f0e-3f51a5c39ee7.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="Trump would gut Biden’s landmark IRA climate law if elected" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/us-presidential-election-2024" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">US presidential election 2024</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="ed4b352b-5c06-4f8d-9df7-1b1f9fecb269" data-is-exclusive="false" data-is-scoop="true">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/ed4b352b-5c06-4f8d-9df7-1b1f9fecb269" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Trump would gut Biden’s landmark IRA climate law if elected</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/ed4b352b-5c06-4f8d-9df7-1b1f9fecb269" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Former president plans to scrap clean energy rules and expand drilling to boost fossil fuels, say advisers</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp"></div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-4 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:hipgnosis-songs-fund;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="hipgnosis-songs-fund" data-trackable-context-storygroup-position="1" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/8c7069fd-70fe-46b2-b082-ca0fb0a618fa" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F6de06306-7a89-48d7-9605-f5814d4d795a.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F6de06306-7a89-48d7-9605-f5814d4d795a.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F6de06306-7a89-48d7-9605-f5814d4d795a.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="Hipgnosis seeks new auditor as it faces legal action " class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/stream/6ba4376c-740a-4ddc-8f62-957b8cde9d74" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Hipgnosis Songs Fund</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="8c7069fd-70fe-46b2-b082-ca0fb0a618fa" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/8c7069fd-70fe-46b2-b082-ca0fb0a618fa" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Hipgnosis seeks new auditor as it faces legal action </span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/8c7069fd-70fe-46b2-b082-ca0fb0a618fa" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">PwC refused to reapply for the job at troubled music rights investor </span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp"></div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-7 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:disease-control-and-prevention;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="disease-control-and-prevention" data-trackable-context-storygroup-position="2" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/c1ef57d8-1e80-47e2-ad49-a56170b3e1c9" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F31ac5d3f-bd3c-4bf4-ae6c-77d64ea3bd3c.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F31ac5d3f-bd3c-4bf4-ae6c-77d64ea3bd3c.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F31ac5d3f-bd3c-4bf4-ae6c-77d64ea3bd3c.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="WHO asks China for data on ‘undiagnosed pneumonia’ cases" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/disease-control-prevention" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Disease control and prevention</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="c1ef57d8-1e80-47e2-ad49-a56170b3e1c9" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/c1ef57d8-1e80-47e2-ad49-a56170b3e1c9" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">WHO asks China for data on ‘undiagnosed pneumonia’ cases</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/c1ef57d8-1e80-47e2-ad49-a56170b3e1c9" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Health body’s concern reflects heightened vigilance over signs of disease outbreaks since Covid pandemic</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp"></div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-10 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:chinese-business-and-finance;storyGroup:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="chinese-business-and-finance" data-trackable-context-storygroup-position="3" data-trackable-context-storygroup-siblings="4" class="layout-desktop--full-height">
                                                    <div id="native-ads-placeholder" class="story-group">
                                                        <div class="grid grid--1-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="2" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-3">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__image primary-story__image--1-cols">
                                                                                    <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/4f46e278-971e-49f0-ab05-47b3a57997ec" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                        <picture>
                                                                                            <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F2c5be13e-386d-4ac0-a6bb-1584f4f28be8.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down"/>
                                                                                            <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F2c5be13e-386d-4ac0-a6bb-1584f4f28be8.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                            <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F2c5be13e-386d-4ac0-a6bb-1584f4f28be8.jpg?source=next-home-page&amp;dpr=2&amp;width=280&amp;fit=scale-down" alt="Chinese shadow bank Zhongzhi faces $36bn shortfall after ‘management ran wild’" class="image image--width-280" loading="lazy"/>
                                                                                        </picture>
                                                                                    </a>
                                                                                </div>
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="story-group__title">
                                                                                        <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/chinese-business-finance" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Chinese business &amp;finance</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="4f46e278-971e-49f0-ab05-47b3a57997ec" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/4f46e278-971e-49f0-ab05-47b3a57997ec" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Chinese shadow bank Zhongzhi faces $36bn shortfall after ‘management ran wild’</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/4f46e278-971e-49f0-ab05-47b3a57997ec" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Financial group tells investors it is ‘severely insolvent’ after unexpected death of its founder in 2021</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp"></div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1 story-group--full-width-1 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="2" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="916fbbcc-8beb-4437-bc09-d4d0bac1fbbf" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/916fbbcc-8beb-4437-bc09-d4d0bac1fbbf" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                    </span>
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Lex. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">China property: running out of options as fallout spreads to shadow banking   </span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <section class="slice advert-slice slice__no-title">
                            <div class="slice__content">
                                <div class="layout-tablet__grid-container">
                                    <div class="layout-tablet__grid layout-tablet__grid--span12 layout-tablet__grid--column-start-1 layout-tablet__grid--row-start-1">
                                        <div class="layout__grid-content">
                                            <pg-slot data-config-key="mid1"></pg-slot>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <div data-trackable="list:opinion" data-trackable-context-list-type="opinion" data-trackable-context-list-position="11" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice slice--default">
                                <div class="slice__content">
                                    <div class="separator--dotted"></div>
                                    <header id="opinion" class="slice-heading">
                                        <h2 class="slice-heading__title">
                                            <a data-trackable="link" data-trackable-context-story-link="link" href="/opinion" class="link" target="_self" aria-hidden="false">
                                                <span class="text text--color-black-80 text-sans--scale-0" id="">Opinion</span>
                                            </a>
                                        </h2>
                                    </header>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span12 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div class="layout-desktop--full-height">
                                                    <div class="layout-desktop__grid-container opinion-section">
                                                        <div class="layout-desktop__grid layout-desktop__grid--span12 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="storyGroupTitle:storygroup;storyGroup:xlarge" data-trackable-context-list-type="opinion" data-trackable-context-storygroup-size="xlarge" data-trackable-context-storygroup-title="storygroup" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="1">
                                                                    <div class="main-opinion-stories main-opinion-stories--theme-featured">
                                                                        <div class="grid grid--12-columns grid--fullHeight">
                                                                            <div class="main-opinion-stories__primary-story">
                                                                                <div data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="2" class="grid grid--9-columns grid--fullHeight">
                                                                                    <div class="primary-opinion-story__wrapper">
                                                                                        <div class="primary-opinion-story__teaser">
                                                                                            <div class="headline js-teaser-headline headline--scale-5 headline--color-black" data-content-id="fb407dcc-24fc-4f3b-b9b7-65fd3f5d29cd" data-is-exclusive="false" data-is-scoop="false">
                                                                                                <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/fb407dcc-24fc-4f3b-b9b7-65fd3f5d29cd" class="link" target="_self" aria-hidden="false">
                                                                                                    <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                                        <span class="icon icon--opinion icon--scale-5">
                                                                                                            <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                                        </span>
                                                                                                    </span>
                                                                                                    <span class="text text--color-black text-display--scale-5 text--weight-400" id="">Jeremy Hunt has not done nearly enough to alleviate hunger and hardship</span>
                                                                                                </a>
                                                                                            </div>
                                                                                            <p class="standfirst">
                                                                                                <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/fb407dcc-24fc-4f3b-b9b7-65fd3f5d29cd" class="link" target="_self" aria-hidden="false">
                                                                                                    <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Some of the UK chancellor’s measures are very welcome — but much more needs to be done </span>
                                                                                                </a>
                                                                                            </p>
                                                                                        </div>
                                                                                        <div class="grid-item grid-item--span-3 grid-item--align-self-end">
                                                                                            <div class="metadata">
                                                                                                <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/stream/099f6372-77cf-4109-9782-d67a3999ee1b" class="link" target="_self" aria-hidden="false">
                                                                                                    <span class="text text--color-black text-sans--scale-0" id="">Helen Barnard</span>
                                                                                                </a>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                    <div class="primary-opinion-story__image">
                                                                                        <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/fb407dcc-24fc-4f3b-b9b7-65fd3f5d29cd" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                            <picture>
                                                                                                <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Feafe71d6-df47-4571-bbbc-b0c54be12d28.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;height=435&amp;fit=cover&amp;gravity=poi"/>
                                                                                                <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Feafe71d6-df47-4571-bbbc-b0c54be12d28.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                                <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Feafe71d6-df47-4571-bbbc-b0c54be12d28.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;height=435&amp;fit=cover&amp;gravity=poi" alt="Jeremy Hunt has not done nearly enough to alleviate hunger and hardship" class="image image--width-580"/>
                                                                                            </picture>
                                                                                        </a>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                            <div class="main-opinion-stories__secondary-story">
                                                                                <div class="separator--solid"></div>
                                                                                <div data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="2" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                                    <div class="grid-item grid-item--span-3">
                                                                                        <div class="grid grid--1-columns grid--s3-spacing">
                                                                                            <div class="primary-story__teaser">
                                                                                                <div class="headline js-teaser-headline headline--scale-3 headline--color-black" data-content-id="a908aa39-85ea-4693-b828-bdcbaf89a5b9" data-is-exclusive="false" data-is-scoop="false">
                                                                                                    <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/a908aa39-85ea-4693-b828-bdcbaf89a5b9" class="link" target="_self" aria-hidden="false">
                                                                                                        <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                                            <span class="icon icon--opinion icon--scale-3">
                                                                                                                <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                                            </span>
                                                                                                            <span class="text text--color-black text-display--scale-3 text--weight-600" id="">Free Lunch. </span>
                                                                                                        </span>
                                                                                                        <span class="text text--color-black text-display--scale-3 text--weight-500" id="">Autumn Statement: a very British (tax) affair</span>
                                                                                                    </a>
                                                                                                </div>
                                                                                                <p class="standfirst">
                                                                                                    <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/a908aa39-85ea-4693-b828-bdcbaf89a5b9" class="link" target="_self" aria-hidden="false">
                                                                                                        <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">The problems with letting the fiscal rule tail wag the budget dog</span>
                                                                                                    </a>
                                                                                                </p>
                                                                                            </div>
                                                                                            <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                                <div class="metadata metadata__opinion">
                                                                                                    <picture>
                                                                                                        <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FMartin_Sandbu-28ef39d5-4a4a-47dc-bdbf-f009445b17c2.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi"/>
                                                                                                        <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FMartin_Sandbu-28ef39d5-4a4a-47dc-bdbf-f009445b17c2.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                                        <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FMartin_Sandbu-28ef39d5-4a4a-47dc-bdbf-f009445b17c2.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi" alt="" class="image image--width-40"/>
                                                                                                    </picture>
                                                                                                    <div class="author-opinion-details">
                                                                                                        <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/martin-sandbu" class="link" target="_self" aria-hidden="false">
                                                                                                            <span class="text text--color-black text-sans--scale-0" id="">Martin Sandbu</span>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span12 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-2 layout-desktop__grid--with-padding">
                                                            <div class="separator--solid"></div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span9 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-3 layout-desktop__grid--with-border">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="storyGroupTitle:storygroup;storyGroup:large" data-trackable-context-list-type="opinion" data-trackable-context-storygroup-size="large" data-trackable-context-storygroup-title="storygroup" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="2">
                                                                    <div class="story-group story-group--skip-primary-story">
                                                                        <div class="grid grid--3-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1">
                                                                                <div class="story-group__article story-group__article--secondary">
                                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="0" data-trackable-context-story-siblings="6" class="grid grid--1-columns grid--s3-spacing">
                                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="108727c5-abd0-4194-b961-2676257a34b9" data-is-exclusive="false" data-is-scoop="false">
                                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/108727c5-abd0-4194-b961-2676257a34b9" class="link" target="_self" aria-hidden="false">
                                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                                    </span>
                                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">FT Magazine. </span>
                                                                                                </span>
                                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">How to tackle your inner climate denier</span>
                                                                                            </a>
                                                                                        </div>
                                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                            <div class="metadata metadata__opinion">
                                                                                                <picture>
                                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Ffthead-v1_simon-kuper-2074514d-b419-4448-b602-1f0924c7462a.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi"/>
                                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Ffthead-v1_simon-kuper-2074514d-b419-4448-b602-1f0924c7462a.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Ffthead-v1_simon-kuper-2074514d-b419-4448-b602-1f0924c7462a.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi" alt="" class="image image--width-40"/>
                                                                                                </picture>
                                                                                                <div class="author-opinion-details">
                                                                                                    <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/simon-kuper" class="link" target="_self" aria-hidden="false">
                                                                                                        <span class="text text--color-black text-sans--scale-0" id="">Simon Kuper</span>
                                                                                                    </a>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="story-group__separator">
                                                                                    <div class="separator--solid"></div>
                                                                                </div>
                                                                            </div>
                                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-2">
                                                                                <div class="story-group__article story-group__article--secondary">
                                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="6" class="grid grid--1-columns grid--s3-spacing">
                                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="3f4f0e67-2825-492a-897d-0691fbb24a27" data-is-exclusive="false" data-is-scoop="false">
                                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/3f4f0e67-2825-492a-897d-0691fbb24a27" class="link" target="_self" aria-hidden="false">
                                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Hunt may be lucky but he has not solved the UK growth challenge</span>
                                                                                            </a>
                                                                                        </div>
                                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                            <div class="metadata metadata__opinion">
                                                                                                <picture>
                                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FMartin_Wolf-7a67b0dc-eac0-4473-9a15-6a0c8317a66d.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi"/>
                                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FMartin_Wolf-7a67b0dc-eac0-4473-9a15-6a0c8317a66d.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FMartin_Wolf-7a67b0dc-eac0-4473-9a15-6a0c8317a66d.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi" alt="" class="image image--width-40"/>
                                                                                                </picture>
                                                                                                <div class="author-opinion-details">
                                                                                                    <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/martin-wolf" class="link" target="_self" aria-hidden="false">
                                                                                                        <span class="text text--color-black text-sans--scale-0" id="">Martin Wolf</span>
                                                                                                    </a>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="story-group__separator">
                                                                                    <div class="separator--solid"></div>
                                                                                </div>
                                                                            </div>
                                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-3 story-group--end-of-row">
                                                                                <div class="story-group__article story-group__article--secondary">
                                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="2" data-trackable-context-story-siblings="6" class="grid grid--1-columns grid--s3-spacing">
                                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="a9ea4937-6a02-4eed-b751-adaca5076d84" data-is-exclusive="false" data-is-scoop="false">
                                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/a9ea4937-6a02-4eed-b751-adaca5076d84" class="link" target="_self" aria-hidden="false">
                                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">A Tory chancellor walks into a bar . . . </span>
                                                                                            </a>
                                                                                        </div>
                                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                            <div class="metadata metadata__opinion">
                                                                                                <picture>
                                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Frobert_shrimsley-ff15e61e-e8c4-4b51-a86e-5706b99741d8.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi"/>
                                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Frobert_shrimsley-ff15e61e-e8c4-4b51-a86e-5706b99741d8.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2Frobert_shrimsley-ff15e61e-e8c4-4b51-a86e-5706b99741d8.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi" alt="" class="image image--width-40"/>
                                                                                                </picture>
                                                                                                <div class="author-opinion-details">
                                                                                                    <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/robert-shrimsley" class="link" target="_self" aria-hidden="false">
                                                                                                        <span class="text text--color-black text-sans--scale-0" id="">Robert Shrimsley</span>
                                                                                                    </a>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="story-group__separator">
                                                                                    <div class="separator--solid"></div>
                                                                                </div>
                                                                            </div>
                                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1">
                                                                                <div class="story-group__article story-group__article--secondary">
                                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="3" data-trackable-context-story-siblings="6" class="grid grid--1-columns grid--s3-spacing">
                                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="5f28228e-8058-4168-9209-70d5f174912d" data-is-exclusive="false" data-is-scoop="false">
                                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/5f28228e-8058-4168-9209-70d5f174912d" class="link" target="_self" aria-hidden="false">
                                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                                    </span>
                                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Outlook. </span>
                                                                                                </span>
                                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Why the race to host world sporting events has slowed to a halt</span>
                                                                                            </a>
                                                                                        </div>
                                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                            <div class="metadata metadata__opinion">
                                                                                                <picture>
                                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FJosh_Noble-d6374cf7-ac12-4c47-bd30-3540f2c08199.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi"/>
                                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FJosh_Noble-d6374cf7-ac12-4c47-bd30-3540f2c08199.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FJosh_Noble-d6374cf7-ac12-4c47-bd30-3540f2c08199.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi" alt="" class="image image--width-40"/>
                                                                                                </picture>
                                                                                                <div class="author-opinion-details">
                                                                                                    <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/josh-noble" class="link" target="_self" aria-hidden="false">
                                                                                                        <span class="text text--color-black text-sans--scale-0" id="">Josh Noble</span>
                                                                                                    </a>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                                    <div class="separator--solid"></div>
                                                                                </div>
                                                                            </div>
                                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-2">
                                                                                <div class="story-group__article story-group__article--secondary">
                                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="4" data-trackable-context-story-siblings="6" class="grid grid--1-columns grid--s3-spacing">
                                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="eb1bb373-07a8-48f8-b5e6-aa3c9ed98e64" data-is-exclusive="false" data-is-scoop="false">
                                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/eb1bb373-07a8-48f8-b5e6-aa3c9ed98e64" class="link" target="_self" aria-hidden="false">
                                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Chinese-made wind farms could become a new sabotage risk</span>
                                                                                            </a>
                                                                                        </div>
                                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                            <div class="metadata">
                                                                                                <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/stream/89a963d8-cf76-3893-88c9-d121dc44bc5f" class="link" target="_self" aria-hidden="false">
                                                                                                    <span class="text text--color-black text-sans--scale-0" id="">Elisabeth Braw</span>
                                                                                                </a>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                                    <div class="separator--solid"></div>
                                                                                </div>
                                                                            </div>
                                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-3 story-group--end-of-row">
                                                                                <div class="story-group__article story-group__article--secondary">
                                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="5" data-trackable-context-story-siblings="6" class="grid grid--1-columns grid--s3-spacing">
                                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="6aae209a-c55d-48ef-9b50-26b446ab82bc" data-is-exclusive="false" data-is-scoop="false">
                                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/6aae209a-c55d-48ef-9b50-26b446ab82bc" class="link" target="_self" aria-hidden="false">
                                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                                    </span>
                                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Trade Secrets. </span>
                                                                                                </span>
                                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">A faint chance of success for Javier Milei</span>
                                                                                            </a>
                                                                                        </div>
                                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                            <div class="metadata metadata__opinion">
                                                                                                <picture>
                                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FAlan-Beattie-4efac6d2-0f5a-4697-9389-77bae75d40eb.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi"/>
                                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FAlan-Beattie-4efac6d2-0f5a-4697-9389-77bae75d40eb.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FAlan-Beattie-4efac6d2-0f5a-4697-9389-77bae75d40eb.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi" alt="" class="image image--width-40"/>
                                                                                                </picture>
                                                                                                <div class="author-opinion-details">
                                                                                                    <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/alan-beattie" class="link" target="_self" aria-hidden="false">
                                                                                                        <span class="text text--color-black text-sans--scale-0" id="">Alan Beattie</span>
                                                                                                    </a>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                                    <div class="separator--solid"></div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-10 layout-desktop__grid--row-start-3">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="storyGroupTitle:opinion;storyGroup:small" data-trackable-context-list-type="opinion" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="opinion" data-trackable-context-storygroup-position="1" data-trackable-context-storygroup-siblings="2">
                                                                    <div class="list list--vertical">
                                                                        <h3 class="text text--color-black text-sans--scale-0 text--weight-600" id="">More Opinion</h3>
                                                                        <ul class="list__items-wrapper">
                                                                            <li>
                                                                                <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="0" data-trackable-context-story-siblings="5" data-id="opinion-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                                    <div class="list__item-link">
                                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/ft-view" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-sans--scale-0" id="">The FT View</span>
                                                                                        </a>
                                                                                    </div>
                                                                                </div>
                                                                            </li>
                                                                            <li>
                                                                                <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="1" data-trackable-context-story-siblings="5" data-id="opinion-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                                    <div class="list__item-link">
                                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/lex" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-sans--scale-0" id="">Lex</span>
                                                                                        </a>
                                                                                    </div>
                                                                                </div>
                                                                            </li>
                                                                            <li>
                                                                                <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="2" data-trackable-context-story-siblings="5" data-id="opinion-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                                    <div class="list__item-link">
                                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/unhedged" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-sans--scale-0" id="">Unhedged</span>
                                                                                        </a>
                                                                                    </div>
                                                                                </div>
                                                                            </li>
                                                                            <li>
                                                                                <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="3" data-trackable-context-story-siblings="5" data-id="opinion-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                                    <div class="list__item-link">
                                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/markets/insight" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-sans--scale-0" id="">Markets Insight</span>
                                                                                        </a>
                                                                                    </div>
                                                                                </div>
                                                                            </li>
                                                                            <li>
                                                                                <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="4" data-trackable-context-story-siblings="5" data-id="opinion-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                                    <div class="list__item-link">
                                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/companies/inside-business" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-sans--scale-0" id="">Inside Business</span>
                                                                                        </a>
                                                                                    </div>
                                                                                </div>
                                                                            </li>
                                                                        </ul>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <div data-trackable="list:uk-news" data-trackable-context-list-type="uk-news" data-trackable-context-list-position="12" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice slice--default">
                                <div class="slice__content">
                                    <div class="separator--dotted"></div>
                                    <header id="uk-news" class="slice-heading">
                                        <h2 class="slice-heading__title">
                                            <a data-trackable="link" data-trackable-context-story-link="link" href="/world/uk" class="link" target="_self" aria-hidden="false">
                                                <span class="text text--color-black-80 text-sans--scale-0" id="">UK News</span>
                                            </a>
                                        </h2>
                                    </header>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span9 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:storygroup;storyGroup:large" data-trackable-context-storygroup-size="large" data-trackable-context-storygroup-title="storygroup" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="2" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--3-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="7" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-1">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="headline js-teaser-headline headline--scale-4 headline--color-black" data-content-id="518e7467-6d93-41bc-bbc2-e9666ba46464" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/518e7467-6d93-41bc-bbc2-e9666ba46464" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-4 text--weight-500" id="">Q &amp;A: How will the Autumn Statement affect me?</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/518e7467-6d93-41bc-bbc2-e9666ba46464" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Experts answer your personal finance questions </span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp timestamp--updated">
                                                                                            <span class="timestamp-prefix">updated  </span>
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T17:22:23+0000"></time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div class="primary-story__image primary-story__image--3-cols">
                                                                            <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/518e7467-6d93-41bc-bbc2-e9666ba46464" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F3f354721-6ab7-460e-bed3-4920081e3e98.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F3f354721-6ab7-460e-bed3-4920081e3e98.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F3f354721-6ab7-460e-bed3-4920081e3e98.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down" alt="Q&amp;A: How will the Autumn Statement affect me?" class="image image--width-580" loading="lazy"/>
                                                                                </picture>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="39b40e8a-464a-4688-bd4c-664f399b31e9" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/39b40e8a-464a-4688-bd4c-664f399b31e9" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">UK energy price cap to rise by 5% in January</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-2">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="2" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="554043b3-a5a1-44d2-a360-5187e1523dc1" data-is-exclusive="false" data-is-scoop="true">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/554043b3-a5a1-44d2-a360-5187e1523dc1" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Hunt criticised for downgrading climate change in BoE guidance </span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="3" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="04faad63-4371-47a2-bb85-726b61fa5820" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/04faad63-4371-47a2-bb85-726b61fa5820" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Virgin Money profits hit by rising bad loan provisions</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-1">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="4" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="eff82cbe-f5a1-4ec4-94c4-8bb5916dfdf2" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/eff82cbe-f5a1-4ec4-94c4-8bb5916dfdf2" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">UK business activity grows marginally in November</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-2">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="5" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="1a27b171-1262-420a-8a48-6b536676c819" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/1a27b171-1262-420a-8a48-6b536676c819" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Nissan set to build two new electric models at its Sunderland plant</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="6" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="12a14570-cb33-4bc2-8262-9ab3ee2ccf78" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/12a14570-cb33-4bc2-8262-9ab3ee2ccf78" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Inside Politics. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Tax cuts today, impossible spending cuts tomorrow</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-10 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="group:uk-news;groupSize:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="uk-news" data-trackable-context-storygroup-position="1" data-trackable-context-storygroup-siblings="2" class="layout-desktop--full-height">
                                                    <div class="links-promo">
                                                        <div class="list list--vertical">
                                                            <h3 class="text text--color-black text-sans--scale-0 text--weight-600" id="">More UK news</h3>
                                                            <ul class="list__items-wrapper">
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="0" data-trackable-context-story-siblings="5" data-id="uk-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/uk-business-economy" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">UK Business &amp;Economy</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="1" data-trackable-context-story-siblings="5" data-id="uk-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/world/uk/politics" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">UK Politics &amp;Policy</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="2" data-trackable-context-story-siblings="5" data-id="uk-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/companies/uk" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">UK Companies</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="3" data-trackable-context-story-siblings="5" data-id="uk-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/brexit" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Brexit</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="4" data-trackable-context-story-siblings="5" data-id="uk-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/personal-finance" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Personal Finance</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                            </ul>
                                                        </div>
                                                        <div data-trackable="story:related-promo" data-trackable-context-story-type="related-promo" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="promo__links">
                                                            <div class="promo__links-text">
                                                                <a data-trackable="related-promo-link" data-trackable-context-story-link="related-promo-link" href="https://www.ft.com/newsletter-signup/inside-politics/promo?segmentId=6e0e1967-2b41-c957-bc2f-1d59a44e3b4a" class="link" target="_self" aria-hidden="false">
                                                                    <span class="text text--color-black text-display--scale-2 text--weight-700" id="">Inside Politics</span>
                                                                    <span class="promo__links--spacing">
                                                                        <span class="text text--color-teal text-sans--scale-0" id="">Sign up for our newsletter</span>
                                                                    </span>
                                                                </a>
                                                            </div>
                                                            <div class="promo__links-image">
                                                                <a data-trackable="related-promo-link" data-trackable-context-story-link="related-promo-link" href="https://www.ft.com/newsletter-signup/inside-politics/promo?segmentId=6e0e1967-2b41-c957-bc2f-1d59a44e3b4a" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                    <picture>
                                                                        <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fwww.ft.com%2F__assets%2Fcreatives%2Fhomepage-beta%2Finside-politics.png?source=next-home-page&amp;dpr=2&amp;width=280&amp;height=280&amp;fit=cover&amp;gravity=poi"/>
                                                                        <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fwww.ft.com%2F__assets%2Fcreatives%2Fhomepage-beta%2Finside-politics.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                        <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fwww.ft.com%2F__assets%2Fcreatives%2Fhomepage-beta%2Finside-politics.png?source=next-home-page&amp;dpr=2&amp;width=280&amp;height=280&amp;fit=cover&amp;gravity=poi" alt="Sign up to our newsletter for Inside Politics." class="image image--width-280"/>
                                                                    </picture>
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <div data-trackable="list:podcasts" data-trackable-context-list-type="podcasts" data-trackable-context-list-position="13" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice story-group-named-slice slice--full-bleed slice--full-bleed--less-top-padding slice--impact">
                                <div class="slice__content">
                                    <header id="podcasts" class="slice-heading">
                                        <h2 class="slice-heading__title">
                                            <a data-trackable="link" data-trackable-context-story-link="link" href="/podcasts" class="link" target="_self" aria-hidden="false">
                                                <span class="text text--color-black-80 text-sans--scale-0" id="">Podcasts</span>
                                            </a>
                                        </h2>
                                    </header>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span12 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout--impact">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:storycollection;storyGroup:xlarge" data-trackable-context-storygroup-size="xlarge" data-trackable-context-storygroup-title="storycollection" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="1" class="layout-desktop--full-height">
                                                    <div class="layout-desktop__grid-container story-collection">
                                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="4" class="grid grid--1-columns grid--s3-spacing grid--fullHeight">
                                                                    <div class="podcast__article-wrapper">
                                                                        <div class="grid-item grid-item--span-3 podcast__image">
                                                                            <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/6e046481-420c-4559-ab9f-8f9f7e90c194" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F5ac06342-b993-47b8-90f5-8ae456e33f67?source=next-home-page&amp;dpr=2&amp;width=180&amp;height=180&amp;fit=cover&amp;gravity=poi"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F5ac06342-b993-47b8-90f5-8ae456e33f67?source=next-home-page&amp;dpr=2&amp;width=580&amp;height=580&amp;fit=cover&amp;gravity=poi"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F5ac06342-b993-47b8-90f5-8ae456e33f67?source=next-home-page&amp;dpr=2&amp;width=180&amp;height=180&amp;fit=cover&amp;gravity=poi" alt="Political Fix podcast" class="image image--width-180"/>
                                                                                </picture>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-3 podcast__content">
                                                                            <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-is-exclusive="false" data-is-scoop="false">
                                                                                <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/6e046481-420c-4559-ab9f-8f9f7e90c194" class="link" target="_self" aria-hidden="false">
                                                                                    <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                        <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Political Fix. </span>
                                                                                    </span>
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-400" id="">Autumn Statement Reaction</span>
                                                                                </a>
                                                                            </div>
                                                                            <div class="podcast__suffix">
                                                                                <span class="text text--color-black-60 text-sans--scale-0" id="">25 min listen</span>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-4 layout-desktop__grid--row-start-1">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="1" data-trackable-context-story-siblings="4" class="grid grid--1-columns grid--s3-spacing grid--fullHeight">
                                                                    <div class="podcast__article-wrapper">
                                                                        <div class="grid-item grid-item--span-3 podcast__image">
                                                                            <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/ddc31999-517a-468c-936e-39dceed4b6a3" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F0ebb729e-269c-4215-af4c-a1c412b4990a?source=next-home-page&amp;dpr=2&amp;width=180&amp;height=180&amp;fit=cover&amp;gravity=poi"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F0ebb729e-269c-4215-af4c-a1c412b4990a?source=next-home-page&amp;dpr=2&amp;width=580&amp;height=580&amp;fit=cover&amp;gravity=poi"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F0ebb729e-269c-4215-af4c-a1c412b4990a?source=next-home-page&amp;dpr=2&amp;width=180&amp;height=180&amp;fit=cover&amp;gravity=poi" alt="Rachman Review podcast" class="image image--width-180"/>
                                                                                </picture>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-3 podcast__content">
                                                                            <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-is-exclusive="false" data-is-scoop="false">
                                                                                <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/ddc31999-517a-468c-936e-39dceed4b6a3" class="link" target="_self" aria-hidden="false">
                                                                                    <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                        <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Rachman Review. </span>
                                                                                    </span>
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-400" id="">How united are Arab and Muslim leaders on Gaza?</span>
                                                                                </a>
                                                                            </div>
                                                                            <div class="podcast__suffix">
                                                                                <span class="text text--color-black-60 text-sans--scale-0" id="">20 min listen</span>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-7 layout-desktop__grid--row-start-1">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="2" data-trackable-context-story-siblings="4" class="grid grid--1-columns grid--s3-spacing grid--fullHeight">
                                                                    <div class="podcast__article-wrapper">
                                                                        <div class="grid-item grid-item--span-3 podcast__image">
                                                                            <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/434c2df7-1f06-4206-9155-49d56d5e4978" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F29f7e2e9-f9e4-440b-885d-7c7e20a73c31?source=next-home-page&amp;dpr=2&amp;width=180&amp;height=180&amp;fit=cover&amp;gravity=poi"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F29f7e2e9-f9e4-440b-885d-7c7e20a73c31?source=next-home-page&amp;dpr=2&amp;width=580&amp;height=580&amp;fit=cover&amp;gravity=poi"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F29f7e2e9-f9e4-440b-885d-7c7e20a73c31?source=next-home-page&amp;dpr=2&amp;width=180&amp;height=180&amp;fit=cover&amp;gravity=poi" alt="FT News Briefing podcast" class="image image--width-180"/>
                                                                                </picture>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-3 podcast__content">
                                                                            <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-is-exclusive="false" data-is-scoop="false">
                                                                                <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/434c2df7-1f06-4206-9155-49d56d5e4978" class="link" target="_self" aria-hidden="false">
                                                                                    <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                        <span class="text text--color-black text-display--scale-2 text--weight-600" id="">FT News Briefing. </span>
                                                                                    </span>
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-400" id="">Ousted OpenAI board member on AI safety concerns</span>
                                                                                </a>
                                                                            </div>
                                                                            <div class="podcast__suffix">
                                                                                <span class="text text--color-black-60 text-sans--scale-0" id="">11 min listen</span>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-10 layout-desktop__grid--row-start-1">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="3" data-trackable-context-story-siblings="4" class="grid grid--1-columns grid--s3-spacing grid--fullHeight">
                                                                    <div class="podcast__article-wrapper">
                                                                        <div class="grid-item grid-item--span-3 podcast__image">
                                                                            <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/a660e6c1-9150-4eef-907f-e6c6935bb93d" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F306404d4-0a1e-45dd-abf0-de6040141ea9?source=next-home-page&amp;dpr=2&amp;width=180&amp;height=180&amp;fit=cover&amp;gravity=poi"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F306404d4-0a1e-45dd-abf0-de6040141ea9?source=next-home-page&amp;dpr=2&amp;width=580&amp;height=580&amp;fit=cover&amp;gravity=poi"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F306404d4-0a1e-45dd-abf0-de6040141ea9?source=next-home-page&amp;dpr=2&amp;width=180&amp;height=180&amp;fit=cover&amp;gravity=poi" alt="Behind the Money podcast" class="image image--width-180"/>
                                                                                </picture>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-3 podcast__content">
                                                                            <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-is-exclusive="false" data-is-scoop="false">
                                                                                <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/a660e6c1-9150-4eef-907f-e6c6935bb93d" class="link" target="_self" aria-hidden="false">
                                                                                    <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                        <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Behind the Money. </span>
                                                                                    </span>
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-400" id="">Best Of: Why companies don &#x27;t want to list in the UK anymore</span>
                                                                                </a>
                                                                            </div>
                                                                            <div class="podcast__suffix">
                                                                                <span class="text text--color-black-60 text-sans--scale-0" id="">20 min listen</span>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <div data-trackable="list:life-and-arts" data-trackable-context-list-type="life-and-arts" data-trackable-context-list-position="14" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice story-group-named-slice slice--default slice--has-sub-navigation">
                                <div class="slice__content">
                                    <div class="separator--dotted"></div>
                                    <header id="life-and-arts" class="slice-heading">
                                        <h2 class="slice-heading__title">
                                            <a data-trackable="link" data-trackable-context-story-link="link" href="/life-arts" class="link" target="_self" aria-hidden="false">
                                                <span class="text text--color-black-80 text-sans--scale-0" id="">Life &amp;Arts</span>
                                            </a>
                                        </h2>
                                    </header>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span12 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:list;storyGroup:xlarge" data-trackable-context-storygroup-size="xlarge" data-trackable-context-storygroup-title="list" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="1" class="layout-desktop--full-height">
                                                    <div class="list list--horizontal">
                                                        <ul class="list__items-wrapper">
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="0" data-trackable-context-story-siblings="9" data-id="life-and-arts-links" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                    <div class="list__item-link">
                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/arts" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-black text-sans--scale-0" id="">Arts</span>
                                                                        </a>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="1" data-trackable-context-story-siblings="9" data-id="life-and-arts-links" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                    <div class="list__item-link">
                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/books" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-black text-sans--scale-0" id="">Books</span>
                                                                        </a>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="2" data-trackable-context-story-siblings="9" data-id="life-and-arts-links" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                    <div class="list__item-link">
                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/food-drink" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-black text-sans--scale-0" id="">Food &amp;Drink</span>
                                                                        </a>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="3" data-trackable-context-story-siblings="9" data-id="life-and-arts-links" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                    <div class="list__item-link">
                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/magazine" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-black text-sans--scale-0" id="">FT Magazine</span>
                                                                        </a>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="4" data-trackable-context-story-siblings="9" data-id="life-and-arts-links" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                    <div class="list__item-link">
                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/style" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-black text-sans--scale-0" id="">Style</span>
                                                                        </a>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="5" data-trackable-context-story-siblings="9" data-id="life-and-arts-links" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                    <div class="list__item-link">
                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/house-home" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-black text-sans--scale-0" id="">House &amp;Home</span>
                                                                        </a>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="6" data-trackable-context-story-siblings="9" data-id="life-and-arts-links" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                    <div class="list__item-link">
                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/travel" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-black text-sans--scale-0" id="">Travel</span>
                                                                        </a>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="7" data-trackable-context-story-siblings="9" data-id="life-and-arts-links" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                    <div class="list__item-link">
                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/globetrotter" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-black text-sans--scale-0" id="">FT Globetrotter</span>
                                                                        </a>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                            <li>
                                                                <div data-trackable="story:list" data-trackable-context-story-type="list" data-trackable-context-story-position="8" data-trackable-context-story-siblings="9" data-id="life-and-arts-links" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                    <div class="list__item-link">
                                                                        <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/htsi" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-black text-sans--scale-0" id="">HTSI</span>
                                                                        </a>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <div data-trackable="list:life-and-arts" data-trackable-context-list-type="life-and-arts" data-trackable-context-list-position="15" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice story-group-named-slice slice__no-title slice--default">
                                <div class="slice__content">
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span12 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:storycollection;storyGroup:xlarge" data-trackable-context-storygroup-size="xlarge" data-trackable-context-storygroup-title="storycollection" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="1" class="layout-desktop--full-height">
                                                    <div class="layout-desktop__grid-container story-collection">
                                                        <div class="layout-desktop__grid layout-desktop__grid--span6 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="5" class="featured-story">
                                                                    <div class="featured-story__image">
                                                                        <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/eed5b4d3-f2b3-42b3-b12d-afdff34bd3fe" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                            <picture>
                                                                                <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe9d8aaba-a607-41dd-bc6d-2e29b23dc480.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe9d8aaba-a607-41dd-bc6d-2e29b23dc480.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe9d8aaba-a607-41dd-bc6d-2e29b23dc480.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down" alt="Baudry Greene, London: ‘This is how I want to eat now’ — review" class="image image--width-580"/>
                                                                            </picture>
                                                                        </a>
                                                                    </div>
                                                                    <div class="featured-story-content">
                                                                        <div class="story-group__title">
                                                                            <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/restaurants" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Restaurants</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="eed5b4d3-f2b3-42b3-b12d-afdff34bd3fe" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/eed5b4d3-f2b3-42b3-b12d-afdff34bd3fe" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">FT Magazine. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-400" id="">Baudry Greene, London: ‘This is how I want to eat now’ — review</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span6 layout-desktop__grid--column-start-7 layout-desktop__grid--row-start-1">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="1" data-trackable-context-story-siblings="5" class="featured-story featured-story--hide-image-on-mobile">
                                                                    <div class="featured-story__image">
                                                                        <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/19504fed-5e39-488f-b5b8-c9a7eb8a6b84" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                            <picture>
                                                                                <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F57c8bec0-8ace-4476-894d-3a8affd3f201.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F57c8bec0-8ace-4476-894d-3a8affd3f201.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F57c8bec0-8ace-4476-894d-3a8affd3f201.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down" alt="Six films to watch this week" class="image image--width-580"/>
                                                                            </picture>
                                                                        </a>
                                                                    </div>
                                                                    <div class="featured-story-content">
                                                                        <div class="story-group__title">
                                                                            <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/film" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Film</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="19504fed-5e39-488f-b5b8-c9a7eb8a6b84" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/19504fed-5e39-488f-b5b8-c9a7eb8a6b84" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Review. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-400" id="">Six films to watch this week</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span12 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-2 layout-desktop__grid--hidden layout-desktop__grid--with-padding">
                                                            <div class="separator--solid"></div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span4 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-3">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="secondary" data-trackable-context-story-position="2" data-trackable-context-story-siblings="5" class="featured-story featured-story--hide-image-on-mobile">
                                                                    <div class="featured-story__image">
                                                                        <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/56ab793a-4ed4-4795-ba11-a76331f9b973" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                            <picture>
                                                                                <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F872f54da-2bd4-4b9c-bb5d-d96fb268a27c.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F872f54da-2bd4-4b9c-bb5d-d96fb268a27c.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F872f54da-2bd4-4b9c-bb5d-d96fb268a27c.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down" alt="How to embrace misfires, setbacks and flops" class="image image--width-580"/>
                                                                            </picture>
                                                                        </a>
                                                                    </div>
                                                                    <div class="featured-story-content">
                                                                        <div class="story-group__title">
                                                                            <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/books" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Books</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="56ab793a-4ed4-4795-ba11-a76331f9b973" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/56ab793a-4ed4-4795-ba11-a76331f9b973" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">FT Books Essay. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-400" id="">How to embrace misfires, setbacks and flops</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span4 layout-desktop__grid--column-start-5 layout-desktop__grid--row-start-3">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="secondary" data-trackable-context-story-position="3" data-trackable-context-story-siblings="5" class="featured-story featured-story--hide-image-on-mobile">
                                                                    <div class="featured-story__image">
                                                                        <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/5edebffb-4992-432e-81c2-f2a2265591e2" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                            <picture>
                                                                                <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe59711c1-906d-4013-bddf-b6a7def3ac54.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe59711c1-906d-4013-bddf-b6a7def3ac54.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fe59711c1-906d-4013-bddf-b6a7def3ac54.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down" alt="Record producer Mr Eazi’s insider’s guide to Cotonou" class="image image--width-580"/>
                                                                            </picture>
                                                                        </a>
                                                                    </div>
                                                                    <div class="featured-story-content">
                                                                        <div class="story-group__title">
                                                                            <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/travel" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Travel</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="5edebffb-4992-432e-81c2-f2a2265591e2" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/5edebffb-4992-432e-81c2-f2a2265591e2" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">HTSI. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-400" id="">Record producer Mr Eazi’s insider’s guide to Cotonou</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span4 layout-desktop__grid--column-start-9 layout-desktop__grid--row-start-3">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="secondary" data-trackable-context-story-position="4" data-trackable-context-story-siblings="5" class="featured-story featured-story--hide-image-on-mobile">
                                                                    <div class="featured-story__image">
                                                                        <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/53436770-3069-405b-9324-72194ddb9949" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                            <picture>
                                                                                <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fc165d3f4-7954-44a9-9479-00d0c262c6bc.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fc165d3f4-7954-44a9-9479-00d0c262c6bc.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fc165d3f4-7954-44a9-9479-00d0c262c6bc.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down" alt="Hot property: five homes for sale where the weather is still warm" class="image image--width-580"/>
                                                                            </picture>
                                                                        </a>
                                                                    </div>
                                                                    <div class="featured-story-content">
                                                                        <div class="story-group__title">
                                                                            <a data-trackable="story-group-title-link" data-trackable-context-story-link="story-group-title-link" href="https://www.ft.com/prime-property" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-claret text-sans--scale-0 text--weight-600" id="">Prime property</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="53436770-3069-405b-9324-72194ddb9949" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/53436770-3069-405b-9324-72194ddb9949" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-400" id="">Hot property: five homes for sale where the weather is still warm</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <div data-trackable="list:video" data-trackable-context-list-type="video" data-trackable-context-list-position="16" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice story-group-named-slice slice--full-bleed slice--full-bleed--less-top-padding slice--dark">
                                <div class="slice__content">
                                    <header id="video" class="slice-heading">
                                        <h2 class="slice-heading__title">
                                            <a data-trackable="link" data-trackable-context-story-link="link" href="/video" class="link" target="_self" aria-hidden="false">
                                                <span class="text text--color-white text-sans--scale-0" id="">Video</span>
                                            </a>
                                        </h2>
                                    </header>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span12 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout--dark">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:storycollection;storyGroup:xlarge" data-trackable-context-storygroup-size="xlarge" data-trackable-context-storygroup-title="storycollection" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="1" class="layout-desktop--full-height">
                                                    <div class="layout-desktop__grid-container story-collection">
                                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="4" class="grid grid--1-columns grid--s3-spacing video__article-wrapper">
                                                                    <div class="grid-item grid-item--span-3 video__image">
                                                                        <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/video/b6908d24-0c39-425c-a1ed-6b2ad7ad70ff" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                            <div class="preview__image--container">
                                                                                <div class="play__icon--wrapper">
                                                                                    <span class="icon icon--play video icon--scale-3">
                                                                                        <span class="o-normalise-visually-hidden">play video content. </span>
                                                                                    </span>
                                                                                </div>
                                                                                <div class="preview__image--wrapper">
                                                                                    <picture>
                                                                                        <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2Fa5a59894-385d-4448-b475-f35d2e2501eb?source=next-home-page&amp;dpr=2&amp;width=180&amp;fit=scale-down"/>
                                                                                        <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2Fa5a59894-385d-4448-b475-f35d2e2501eb?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                        <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2Fa5a59894-385d-4448-b475-f35d2e2501eb?source=next-home-page&amp;dpr=2&amp;width=180&amp;fit=scale-down" alt="FT Moral Money: The Lithium Mining Race" class="image image--width-180"/>
                                                                                    </picture>
                                                                                </div>
                                                                            </div>
                                                                        </a>
                                                                    </div>
                                                                    <div class="grid-item grid-item--span-3 video__content">
                                                                        <a data-trackable="link" data-trackable-context-story-link="link" href="https://www.ft.com/stream/d23cab6f-a0b8-4136-baa3-1f843b593433" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-white text-sans--scale-0 text--weight-600" id="">
                                                                                <span class="video__content--displayTag">Lithium</span>
                                                                            </span>
                                                                        </a>
                                                                        <span class="text text--color-white text-sans--scale-0 text--weight-400" id="">
                                                                            <span>28 min</span>
                                                                        </span>
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-white" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/video/b6908d24-0c39-425c-a1ed-6b2ad7ad70ff" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="icon icon--video icon--scale-2">
                                                                                        <span class="o-normalise-visually-hidden">video content. </span>
                                                                                    </span>
                                                                                </span>
                                                                                <span class="text text--color-white text-display--scale-2 text--weight-400" id="">Inside the global race for lithium batteries | FT Film</span>
                                                                            </a>
                                                                        </div>
                                                                        <span class="text text--color-white text-sans--scale-2" id="">
                                                                            <div class="timestamp">
                                                                                <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-24-hours" dateTime="2023-11-20T04:59:47+0000">85 hours ago</time>
                                                                            </div>
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-4 layout-desktop__grid--row-start-1">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="1" data-trackable-context-story-siblings="4" class="grid grid--1-columns grid--s3-spacing video__article-wrapper">
                                                                    <div class="grid-item grid-item--span-3 video__image">
                                                                        <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/video/82d06d33-6328-4298-9480-3759fda3821d" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                            <div class="preview__image--container">
                                                                                <div class="play__icon--wrapper">
                                                                                    <span class="icon icon--play video icon--scale-3">
                                                                                        <span class="o-normalise-visually-hidden">play video content. </span>
                                                                                    </span>
                                                                                </div>
                                                                                <div class="preview__image--wrapper">
                                                                                    <picture>
                                                                                        <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2Fe0a716e1-723d-4d3f-8ed0-e1979d3bef94?source=next-home-page&amp;dpr=2&amp;width=180&amp;fit=scale-down"/>
                                                                                        <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2Fe0a716e1-723d-4d3f-8ed0-e1979d3bef94?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                        <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2Fe0a716e1-723d-4d3f-8ed0-e1979d3bef94?source=next-home-page&amp;dpr=2&amp;width=180&amp;fit=scale-down" alt="Sketchy politics: The battleground" class="image image--width-180"/>
                                                                                    </picture>
                                                                                </div>
                                                                            </div>
                                                                        </a>
                                                                    </div>
                                                                    <div class="grid-item grid-item--span-3 video__content">
                                                                        <a data-trackable="link" data-trackable-context-story-link="link" href="https://www.ft.com/uk-general-election" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-white text-sans--scale-0 text--weight-600" id="">
                                                                                <span class="video__content--displayTag">UK general election</span>
                                                                            </span>
                                                                        </a>
                                                                        <span class="text text--color-white text-sans--scale-0 text--weight-400" id="">
                                                                            <span>26 min</span>
                                                                        </span>
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-white" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/video/82d06d33-6328-4298-9480-3759fda3821d" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                    </span>
                                                                                </span>
                                                                                <span class="text text--color-white text-display--scale-2 text--weight-400" id="">Sketchy Politics: mapping the next election | FT</span>
                                                                            </a>
                                                                        </div>
                                                                        <span class="text text--color-white text-sans--scale-2" id="">
                                                                            <div class="timestamp">
                                                                                <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-24-hours" dateTime="2023-11-07T04:58:47+0000">397 hours ago</time>
                                                                            </div>
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-7 layout-desktop__grid--row-start-1">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="2" data-trackable-context-story-siblings="4" class="grid grid--1-columns grid--s3-spacing video__article-wrapper">
                                                                    <div class="grid-item grid-item--span-3 video__image">
                                                                        <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/video/bc00595a-1198-4417-88cc-ea4bd07bf583" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                            <div class="preview__image--container">
                                                                                <div class="play__icon--wrapper">
                                                                                    <span class="icon icon--play video icon--scale-3">
                                                                                        <span class="o-normalise-visually-hidden">play video content. </span>
                                                                                    </span>
                                                                                </div>
                                                                                <div class="preview__image--wrapper">
                                                                                    <picture>
                                                                                        <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2Fa78daf44-c5f4-4066-abb2-577c663621f0?source=next-home-page&amp;dpr=2&amp;width=180&amp;fit=scale-down"/>
                                                                                        <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2Fa78daf44-c5f4-4066-abb2-577c663621f0?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                        <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2Fa78daf44-c5f4-4066-abb2-577c663621f0?source=next-home-page&amp;dpr=2&amp;width=180&amp;fit=scale-down" alt="China and the world BRI - success or failure?" class="image image--width-180"/>
                                                                                    </picture>
                                                                                </div>
                                                                            </div>
                                                                        </a>
                                                                    </div>
                                                                    <div class="grid-item grid-item--span-3 video__content">
                                                                        <a data-trackable="link" data-trackable-context-story-link="link" href="https://www.ft.com/belt-and-road-initiative" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-white text-sans--scale-0 text--weight-600" id="">
                                                                                <span class="video__content--displayTag">Belt and Road Initiative</span>
                                                                            </span>
                                                                        </a>
                                                                        <span class="text text--color-white text-sans--scale-0 text--weight-400" id="">
                                                                            <span>11 min</span>
                                                                        </span>
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-white" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/video/bc00595a-1198-4417-88cc-ea4bd07bf583" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="icon icon--video icon--scale-2">
                                                                                        <span class="o-normalise-visually-hidden">video content. </span>
                                                                                    </span>
                                                                                </span>
                                                                                <span class="text text--color-white text-display--scale-2 text--weight-400" id="">Has China &#x27;s Belt and Road Initiative been a success?</span>
                                                                            </a>
                                                                        </div>
                                                                        <span class="text text--color-white text-sans--scale-2" id="">
                                                                            <div class="timestamp">
                                                                                <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-24-hours" dateTime="2023-10-30T09:30:04+0000">584 hours ago</time>
                                                                            </div>
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-10 layout-desktop__grid--row-start-1">
                                                            <div class="layout__grid-content">
                                                                <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="3" data-trackable-context-story-siblings="4" class="grid grid--1-columns grid--s3-spacing video__article-wrapper">
                                                                    <div class="grid-item grid-item--span-3 video__image">
                                                                        <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/video/daa5f78b-12c5-4e11-8e52-a8baf28a6578" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                            <div class="preview__image--container">
                                                                                <div class="play__icon--wrapper">
                                                                                    <span class="icon icon--play video icon--scale-3">
                                                                                        <span class="o-normalise-visually-hidden">play video content. </span>
                                                                                    </span>
                                                                                </div>
                                                                                <div class="preview__image--wrapper">
                                                                                    <picture>
                                                                                        <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F518facc3-2969-4472-a8d0-4abddabd8b1a?source=next-home-page&amp;dpr=2&amp;width=180&amp;fit=scale-down"/>
                                                                                        <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F518facc3-2969-4472-a8d0-4abddabd8b1a?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                        <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fnext-video-editor-images.s3.ap-northeast-1.amazonaws.com%2F518facc3-2969-4472-a8d0-4abddabd8b1a?source=next-home-page&amp;dpr=2&amp;width=180&amp;fit=scale-down" alt="FT Film: Moon Rush" class="image image--width-180"/>
                                                                                    </picture>
                                                                                </div>
                                                                            </div>
                                                                        </a>
                                                                    </div>
                                                                    <div class="grid-item grid-item--span-3 video__content">
                                                                        <a data-trackable="link" data-trackable-context-story-link="link" href="https://www.ft.com/space-industry" class="link" target="_self" aria-hidden="false">
                                                                            <span class="text text--color-white text-sans--scale-0 text--weight-600" id="">
                                                                                <span class="video__content--displayTag">Space industry</span>
                                                                            </span>
                                                                        </a>
                                                                        <span class="text text--color-white text-sans--scale-0 text--weight-400" id="">
                                                                            <span>27 min</span>
                                                                        </span>
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-white" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/video/daa5f78b-12c5-4e11-8e52-a8baf28a6578" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="icon icon--video icon--scale-2">
                                                                                        <span class="o-normalise-visually-hidden">video content. </span>
                                                                                    </span>
                                                                                </span>
                                                                                <span class="text text--color-white text-display--scale-2 text--weight-400" id="">Moon rush: the launch of a lunar economy | FT Film</span>
                                                                            </a>
                                                                        </div>
                                                                        <span class="text text--color-white text-sans--scale-2" id="">
                                                                            <div class="timestamp">
                                                                                <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-24-hours" dateTime="2023-10-19T02:59:47+0000">855 hours ago</time>
                                                                            </div>
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <div data-trackable="list:highlights" data-trackable-context-list-type="highlights" data-trackable-context-list-position="17" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice slice--default">
                                <div class="slice__content">
                                    <div class="separator--dotted"></div>
                                    <header id="highlights" class="slice-heading">
                                        <h2 class="slice-heading__title">
                                            <span class="text text--color-black-80 text-sans--scale-0" id="">Highlights</span>
                                        </h2>
                                    </header>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span9 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:storygroup;storyGroup:large" data-trackable-context-storygroup-size="large" data-trackable-context-storygroup-title="storygroup" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="2" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--3-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="7" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-1">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="headline js-teaser-headline headline--scale-4 headline--color-black" data-content-id="c14581c7-60ef-4921-a640-640a3d6ef9d6" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/c14581c7-60ef-4921-a640-640a3d6ef9d6" class="link" target="_self" aria-hidden="false">
                                                                                            <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                                <span class="text text--color-black text-display--scale-4 text--weight-600" id="">The Big Read. </span>
                                                                                            </span>
                                                                                            <span class="text text--color-black text-display--scale-4 text--weight-500" id="">Can Disney rediscover the magic?</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/c14581c7-60ef-4921-a640-640a3d6ef9d6" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">In his second act, Bob Iger must overcome streaming losses and investor pressure to pull off a new era of creativity</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp"></div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div class="primary-story__image primary-story__image--3-cols">
                                                                            <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/c14581c7-60ef-4921-a640-640a3d6ef9d6" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F22251731-4ce3-4c61-bdd7-d8740fd7a808.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F22251731-4ce3-4c61-bdd7-d8740fd7a808.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F22251731-4ce3-4c61-bdd7-d8740fd7a808.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down" alt="Can Disney rediscover the magic?" class="image image--width-580" loading="lazy"/>
                                                                                </picture>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="574f0940-d82e-4e4a-98bd-271058cce434" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/574f0940-d82e-4e4a-98bd-271058cce434" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">The Big Read. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Downfall of the judge who dominated US bankruptcy</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-2">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="2" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="0eb7cb51-6ccb-4277-b457-a0ad86c2ba68" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/0eb7cb51-6ccb-4277-b457-a0ad86c2ba68" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Review. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Business Books: What to read this month</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="3" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="413ebae1-00ee-4e60-b6ed-0274c0864da1" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/413ebae1-00ee-4e60-b6ed-0274c0864da1" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Dear Jonathan. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Should I stick with corporate law or switch to something more fulfilling?</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-1">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="4" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="6ee16212-c748-44df-8698-b646f722deb7" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/6ee16212-c748-44df-8698-b646f722deb7" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">The Henry Mance Interview. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Brexit negotiator Michel Barnier: ‘The EU is not the same one the UK left’</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-2">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="5" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="c42006d9-f3c6-4b5a-a42d-f32f7be9915c" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/c42006d9-f3c6-4b5a-a42d-f32f7be9915c" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                    </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">In search of chief executives who never grow ‘old’</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__opinion">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FAndrewHill-7bf7bbc8-e2ed-412e-8fd1-c61bc130c753.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FAndrewHill-7bf7bbc8-e2ed-412e-8fd1-c61bc130c753.png?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2Fuploaded-files%2FAndrewHill-7bf7bbc8-e2ed-412e-8fd1-c61bc130c753.png?source=next-home-page&amp;dpr=2&amp;width=40&amp;height=40&amp;fit=cover&amp;gravity=poi" alt="" class="image image--width-40"/>
                                                                                </picture>
                                                                                <div class="author-opinion-details">
                                                                                    <a data-trackable="author-link" data-trackable-context-story-link="author-link" href="https://www.ft.com/andrew-hill" class="link" target="_self" aria-hidden="false">
                                                                                        <span class="text text--color-black text-sans--scale-0" id="">Andrew Hill</span>
                                                                                    </a>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="6" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="79f0d181-bdae-4c81-a971-861ccd8d512c" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/79f0d181-bdae-4c81-a971-861ccd8d512c" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">The Big Read. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">The violent gang crisis shaking Sweden</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-10 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="group:highlights;groupSize:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="highlights" data-trackable-context-storygroup-position="1" data-trackable-context-storygroup-siblings="2" class="layout-desktop--full-height">
                                                    <div class="links-promo">
                                                        <div class="list list--vertical">
                                                            <h3 class="text text--color-black text-sans--scale-0 text--weight-600" id="">More highlights</h3>
                                                            <ul class="list__items-wrapper">
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="0" data-trackable-context-story-siblings="5" data-id="highlights-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/moral-money" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Moral Money</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="1" data-trackable-context-story-siblings="5" data-id="highlights-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/due-diligence" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Due Diligence</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="2" data-trackable-context-story-siblings="5" data-id="highlights-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/cryptocurrencies" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Cryptocurrencies</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="3" data-trackable-context-story-siblings="5" data-id="highlights-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/reports" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Special Reports</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="4" data-trackable-context-story-siblings="5" data-id="highlights-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/climate-capital" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Climate Capital</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                            </ul>
                                                        </div>
                                                        <div data-trackable="story:related-promo" data-trackable-context-story-type="related-promo" data-trackable-context-story-position="0" data-trackable-context-story-siblings="1" class="promo__links">
                                                            <div class="promo__links-text">
                                                                <a data-trackable="related-promo-link" data-trackable-context-story-link="related-promo-link" href="https://ep.ft.com/newsletters/5ce7dcb373511b000490ac5b/subscribe" class="link" target="_self" aria-hidden="false">
                                                                    <span class="text text--color-black text-display--scale-2 text--weight-700" id="">Moral Money</span>
                                                                    <span class="promo__links--spacing">
                                                                        <span class="text text--color-teal text-sans--scale-0" id="">Sign up for our newsletter</span>
                                                                    </span>
                                                                </a>
                                                            </div>
                                                            <div class="promo__links-image">
                                                                <a data-trackable="related-promo-link" data-trackable-context-story-link="related-promo-link" href="https://ep.ft.com/newsletters/5ce7dcb373511b000490ac5b/subscribe" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                    <picture>
                                                                        <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fwww.ft.com%2F__assets%2Fcreatives%2Fhomepage-beta%2Fmoral-money-promo.jpeg?source=next-home-page&amp;dpr=2&amp;width=280&amp;height=280&amp;fit=cover&amp;gravity=poi"/>
                                                                        <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fwww.ft.com%2F__assets%2Fcreatives%2Fhomepage-beta%2Fmoral-money-promo.jpeg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                        <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fwww.ft.com%2F__assets%2Fcreatives%2Fhomepage-beta%2Fmoral-money-promo.jpeg?source=next-home-page&amp;dpr=2&amp;width=280&amp;height=280&amp;fit=cover&amp;gravity=poi" alt="Sign up to our newsletter for Moral Money." class="image image--width-280"/>
                                                                    </picture>
                                                                </a>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <div data-trackable="list:markets-news" data-trackable-context-list-type="markets-news" data-trackable-context-list-position="18" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice slice--default">
                                <div class="slice__content">
                                    <div class="separator--dotted"></div>
                                    <header id="markets-news" class="slice-heading">
                                        <h2 class="slice-heading__title">
                                            <a data-trackable="link" data-trackable-context-story-link="link" href="/markets" class="link" target="_self" aria-hidden="false">
                                                <span class="text text--color-black-80 text-sans--scale-0" id="">Markets News</span>
                                            </a>
                                        </h2>
                                    </header>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span9 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:storygroup;storyGroup:large" data-trackable-context-storygroup-size="large" data-trackable-context-storygroup-title="storygroup" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="2" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--3-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="7" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-1">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="headline js-teaser-headline headline--scale-4 headline--color-black" data-content-id="fe528c26-a39c-4488-bbb7-5feaa5ed3b54" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/fe528c26-a39c-4488-bbb7-5feaa5ed3b54" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black text-display--scale-4 text--weight-500" id="">Binance’s crypto dominance under threat after loss of founder Zhao</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/fe528c26-a39c-4488-bbb7-5feaa5ed3b54" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">US compliance squeeze means new chief executive Richard Teng will be hard-pressed to keep exchange competitive</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp"></div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div class="primary-story__image primary-story__image--3-cols">
                                                                            <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/fe528c26-a39c-4488-bbb7-5feaa5ed3b54" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F9b641dea-f969-49c1-b286-e29f3f99a35e.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F9b641dea-f969-49c1-b286-e29f3f99a35e.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F9b641dea-f969-49c1-b286-e29f3f99a35e.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down" alt="Binance’s crypto dominance under threat after loss of founder Zhao" class="image image--width-580" loading="lazy"/>
                                                                                </picture>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="dddd51c4-7c5b-4488-b935-6099788bbc89" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/dddd51c4-7c5b-4488-b935-6099788bbc89" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Hedge fund short sellers suffer $43bn of losses in market rally</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-2">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="2" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="eb2afff9-7218-4781-95db-681eddb82240" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/eb2afff9-7218-4781-95db-681eddb82240" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Gilt yields rise as UK plans to borrow more than expected</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="3" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="6d66d428-6f93-4b78-bb6e-6a0377614a2d" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/6d66d428-6f93-4b78-bb6e-6a0377614a2d" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Oil price falls as Opec+ postpones meeting</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-1">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="4" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="49cf74bd-b298-482f-8bbd-b11cacd9cc51" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/49cf74bd-b298-482f-8bbd-b11cacd9cc51" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Investors pour cash into US corporate debt in bet Fed rates have peaked</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-2">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="5" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="d10af983-1376-457f-9709-815e04ba59fb" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/d10af983-1376-457f-9709-815e04ba59fb" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Binance chief resigns as crypto exchange pays $4bn in fines</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="6" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="760afc0a-8c5d-4b16-a92a-624d714c54a2" data-is-exclusive="false" data-is-scoop="true">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/760afc0a-8c5d-4b16-a92a-624d714c54a2" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Blackstone to shut multi-strategy fund after assets fall 90%</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-10 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="group:markets-news;groupSize:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="markets-news" data-trackable-context-storygroup-position="1" data-trackable-context-storygroup-siblings="2" class="layout-desktop--full-height">
                                                    <div class="links-promo">
                                                        <div class="list list--vertical">
                                                            <h3 class="text text--color-black text-sans--scale-0 text--weight-600" id="">More markets news</h3>
                                                            <ul class="list__items-wrapper">
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="0" data-trackable-context-story-siblings="11" data-id="markets-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/alphaville" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Alphaville</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="1" data-trackable-context-story-siblings="11" data-id="markets-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://markets.ft.com/data" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Markets Data</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="2" data-trackable-context-story-siblings="11" data-id="markets-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/capital-markets" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Capital Markets</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="3" data-trackable-context-story-siblings="11" data-id="markets-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/commodities" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Commodities</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="4" data-trackable-context-story-siblings="11" data-id="markets-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/currencies" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Currencies</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="5" data-trackable-context-story-siblings="11" data-id="markets-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/equities" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Equities</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="6" data-trackable-context-story-siblings="11" data-id="markets-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/fund-management" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Fund Management</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="7" data-trackable-context-story-siblings="11" data-id="markets-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/ft-wealth-management" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Wealth Management</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="8" data-trackable-context-story-siblings="11" data-id="markets-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/ft-trading-room" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Trading</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="9" data-trackable-context-story-siblings="11" data-id="markets-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/moral-money" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Moral Money</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="10" data-trackable-context-story-siblings="11" data-id="markets-news-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://etf.ft.com/" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">ETF Hub</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                            </ul>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <div data-trackable="list:technology" data-trackable-context-list-type="technology" data-trackable-context-list-position="19" data-trackable-context-list-siblings="20" class="story-group-slice">
                            <section class="slice slice--default">
                                <div class="slice__content">
                                    <div class="separator--dotted"></div>
                                    <header id="technology" class="slice-heading">
                                        <h2 class="slice-heading__title">
                                            <a data-trackable="link" data-trackable-context-story-link="link" href="/technology" class="link" target="_self" aria-hidden="false">
                                                <span class="text text--color-black-80 text-sans--scale-0" id="">Technology</span>
                                            </a>
                                        </h2>
                                    </header>
                                    <div class="layout-desktop__grid-container">
                                        <div class="layout-desktop__grid layout-desktop__grid--span9 layout-desktop__grid--column-start-1 layout-desktop__grid--row-start-1 layout-desktop__grid--with-border layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="storyGroupTitle:storygroup;storyGroup:large" data-trackable-context-storygroup-size="large" data-trackable-context-storygroup-title="storygroup" data-trackable-context-storygroup-position="0" data-trackable-context-storygroup-siblings="2" class="layout-desktop--full-height">
                                                    <div class="story-group">
                                                        <div class="grid grid--3-columns grid--fullHeight" style="grid-template-rows:min-content;-ms-grid-rows:min-content">
                                                            <div class="story-group__article-wrapper story-group--row-start-1 story-group--column-start-1 story-group--full-width-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--lead">
                                                                    <div data-trackable="story:lead" data-trackable-context-story-type="lead" data-trackable-context-story-position="0" data-trackable-context-story-siblings="7" class="grid grid--3-columns grid--s4-spacing grid--fullHeight">
                                                                        <div class="grid-item grid-item--span-1">
                                                                            <div class="grid grid--1-columns grid--s3-spacing">
                                                                                <div class="primary-story__teaser">
                                                                                    <div class="headline js-teaser-headline headline--scale-4 headline--color-black" data-content-id="b838de69-19cf-4737-9554-e1824d3e2f8b" data-is-exclusive="false" data-is-scoop="false">
                                                                                        <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/b838de69-19cf-4737-9554-e1824d3e2f8b" class="link" target="_self" aria-hidden="false">
                                                                                            <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                                <span class="icon icon--opinion icon--scale-4">
                                                                                                    <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                                </span>
                                                                                                <span class="text text--color-black text-display--scale-4 text--weight-600" id="">Lex. </span>
                                                                                            </span>
                                                                                            <span class="text text--color-black text-display--scale-4 text--weight-500" id="">IPOs: start-ups that missed their moment risk alienating employees</span>
                                                                                        </a>
                                                                                    </div>
                                                                                    <p class="standfirst">
                                                                                        <a data-trackable="standfirst-link" data-trackable-context-story-link="standfirst-link" href="/content/b838de69-19cf-4737-9554-e1824d3e2f8b" class="link" target="_self" aria-hidden="false">
                                                                                            <span class="text text--color-black-60 text-sans--scale-0 text--style--no-active-state" id="">Dearth of listings has meant a lack of exits for staff with stock options</span>
                                                                                        </a>
                                                                                    </p>
                                                                                </div>
                                                                                <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                                    <div class="metadata metadata__timestamp">
                                                                                        <div class="timestamp">
                                                                                            <time class="timestamp-date o-date" data-o-component="o-date" data-o-date-format="time-ago-limit-4-hours" dateTime="2023-11-23T15:59:00+0000">2 hours ago</time>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div class="primary-story__image primary-story__image--3-cols">
                                                                            <a data-trackable="image-link" data-trackable-context-story-link="image-link" href="/content/b838de69-19cf-4737-9554-e1824d3e2f8b" class="link" target="_self" tabindex="-1" aria-hidden="true">
                                                                                <picture>
                                                                                    <source media="(min-width: 1024px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F565dbff7-7e99-42eb-9d96-4ff78f022923.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <source media="(max-width: 580px)" srcSet="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F565dbff7-7e99-42eb-9d96-4ff78f022923.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down"/>
                                                                                    <img src="https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F565dbff7-7e99-42eb-9d96-4ff78f022923.jpg?source=next-home-page&amp;dpr=2&amp;width=580&amp;fit=scale-down" alt="IPOs: start-ups that missed their moment risk alienating employees" class="image image--width-580" loading="lazy"/>
                                                                                </picture>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-1">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="1" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="40769279-972a-4667-b405-0536119aafae" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/40769279-972a-4667-b405-0536119aafae" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="icon icon--opinion icon--scale-2">
                                                                                        <span class="o-normalise-visually-hidden">opinion content. </span>
                                                                                    </span>
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">Lex. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Resonac: fertilising growth for the chip industry   </span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-2">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="2" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="22cb62d7-1b11-466d-8146-79cbdfc05875" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/22cb62d7-1b11-466d-8146-79cbdfc05875" class="link" target="_self" aria-hidden="false">
                                                                                <span placeholder="headlineIndicator" class="headline-indicator">
                                                                                    <span class="text text--color-black text-display--scale-2 text--weight-600" id="">#techAsia. </span>
                                                                                </span>
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Microsoft’s chip move and Disney’s India dilemma</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-2 story-group--column-start-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="3" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="a9b43514-9bef-42eb-92a0-f8af76c56816" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/a9b43514-9bef-42eb-92a0-f8af76c56816" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">How Silicon Valley reunited Sam Altman and OpenAI</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-1">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="4" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="bdd127e4-0b6e-4047-b038-74c1324d8073" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/bdd127e4-0b6e-4047-b038-74c1324d8073" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">AI and quantum research at centre of science and tech announcements</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-2">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="5" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="86a5c3d8-e980-42b0-a1a0-48c3a1306367" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/86a5c3d8-e980-42b0-a1a0-48c3a1306367" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">Can AI improve UK public sector productivity?</span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                            <div class="story-group__article-wrapper story-group--row-start-3 story-group--column-start-3 story-group--end-of-row">
                                                                <div class="story-group__article story-group__article--secondary">
                                                                    <div data-trackable="story:secondary" data-trackable-context-story-type="secondary" data-trackable-context-story-position="6" data-trackable-context-story-siblings="7" class="grid grid--1-columns grid--s3-spacing">
                                                                        <div class="headline js-teaser-headline headline--scale-2 headline--color-black" data-content-id="f89e0067-70a9-49d3-b562-e57cec432462" data-is-exclusive="false" data-is-scoop="false">
                                                                            <a data-trackable="heading-link" data-trackable-context-story-link="heading-link" href="/content/f89e0067-70a9-49d3-b562-e57cec432462" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-display--scale-2 text--weight-500" id="">UK payment sector urged to develop system to bypass dominant card networks </span>
                                                                            </a>
                                                                        </div>
                                                                        <div class="grid-item grid-item--span-1 grid-item--align-self-end">
                                                                            <div class="metadata metadata__timestamp"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="story-group__separator story-group__separator--hidden">
                                                                    <div class="separator--solid"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="layout-desktop__grid layout-desktop__grid--span3 layout-desktop__grid--column-start-10 layout-desktop__grid--row-start-1 layout--default">
                                            <div class="layout__grid-content">
                                                <div data-trackable="group:technology;groupSize:small" data-trackable-context-storygroup-size="small" data-trackable-context-storygroup-title="technology" data-trackable-context-storygroup-position="1" data-trackable-context-storygroup-siblings="2" class="layout-desktop--full-height">
                                                    <div class="links-promo">
                                                        <div class="list list--vertical">
                                                            <h3 class="text text--color-black text-sans--scale-0 text--weight-600" id="">More technology</h3>
                                                            <ul class="list__items-wrapper">
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="0" data-trackable-context-story-siblings="7" data-id="technology-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/cryptofinance" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Cryptofinance</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="1" data-trackable-context-story-siblings="7" data-id="technology-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/semiconductors" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Semiconductors</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="2" data-trackable-context-story-siblings="7" data-id="technology-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/tech-tonic" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Tech Tonic podcast</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="3" data-trackable-context-story-siblings="7" data-id="technology-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/trading-technology" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Trading technology</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="4" data-trackable-context-story-siblings="7" data-id="technology-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/tech-start-ups" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Tech start-ups</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="5" data-trackable-context-story-siblings="7" data-id="technology-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/social-media" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Social Media</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                                <li>
                                                                    <div data-trackable="story:related-link" data-trackable-context-story-type="related-link" data-trackable-context-story-position="6" data-trackable-context-story-siblings="7" data-id="technology-links-promo" data-name="list" data-type="list" data-subtype="" class="list__links">
                                                                        <div class="list__item-link">
                                                                            <a data-trackable="related-link" data-trackable-context-story-link="related-link" href="https://www.ft.com/artificial-intelligence" class="link" target="_self" aria-hidden="false">
                                                                                <span class="text text--color-black text-sans--scale-0" id="">Artificial intelligence</span>
                                                                            </a>
                                                                        </div>
                                                                    </div>
                                                                </li>
                                                            </ul>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <section class="slice section">
                            <div class="slice__content">
                                <div class="separator--dotted"></div>
                                <header id="explore-more-events-from-the-ft" class="slice-heading">
                                    <h2 class="slice-heading__title">
                                        <a data-trackable="link" data-trackable-context-story-link="link" href="https://events.ft.com/events-list" class="link" target="_self" aria-hidden="false">
                                            <span class="text text--color-black-80 text-sans--scale-0" id="">Explore more events from the FT</span>
                                        </a>
                                    </h2>
                                </header>
                                <div class="community-home-page-slice o-grid-row o-grid-row--compact community-home-page-slice--events community-home-page-slice--default-layout">
                                    <div data-o-grid-colspan="12 M12 L3" class="community-home-page-slice__column community-home-page-slice__header-column">
                                        <div class="community-home-page-slice__header">
                                            <div role="heading" aria-level="3" class="community-home-page-slice__title">Upcoming events</div>
                                            <p class="community-home-page-slice__strapline">Discover unmissable flagship events with FT journalists to expand your thinking and elevate your career</p>
                                            <a class="community-home-page-slice__link" href="https://events.ft.com/events-list">Explore all events</a>
                                        </div>
                                    </div>
                                    <div data-o-grid-colspan="12 M4 L3" class="community-home-page-slice__column community-home-page-slice__item-column">
                                        <div class="event-teaser" data-trackable="event-teaser" data-trackable-context-content-id="690acc25-c33b-4f3f-9784-3966205c01d4" data-o-tracking-view="true">
                                            <div class="event-teaser__content-container">
                                                <div class="event-teaser__details">
                                                    <a class="event-teaser__brand" href="https://banking.live.ft.com" data-trackable="event-teaser-brand-link">FT Live</a>
                                                    <div class="event-teaser__title-heading" role="heading" aria-level="4">
                                                        <a class="event-teaser__title" data-trackable="event-teaser-title" href="https://banking.live.ft.com" title="Global Banking Summit">Global Banking Summit</a>
                                                    </div>
                                                    <span class="event-teaser__standfirst">Leadership strategies for the future of banking</span>
                                                </div>
                                                <div class="event-teaser__footer">
                                                    <span class="event-teaser__timestamp event-teaser__timestamp--start-date">
                                                        <time dateTime="2023-11-27T09:00:00.000Z">Monday, 27 November</time>
                                                    </span>
                                                    <span class="event-teaser__location">London, UK</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div data-o-grid-colspan="12 M4 L3" class="community-home-page-slice__column community-home-page-slice__item-column">
                                        <div class="event-teaser" data-trackable="event-teaser" data-trackable-context-content-id="1f200463-5ac0-4a1c-b3d0-351d60f23187" data-o-tracking-view="true">
                                            <div class="event-teaser__content-container">
                                                <div class="event-teaser__details">
                                                    <a class="event-teaser__brand" href="https://events.bizzabo.com/527163" data-trackable="event-teaser-brand-link">FT Live</a>
                                                    <div class="event-teaser__title-heading" role="heading" aria-level="4">
                                                        <a class="event-teaser__title" data-trackable="event-teaser-title" href="https://events.bizzabo.com/527163" title="Women at the Top Italy Summit">Women at the Top Italy Summit</a>
                                                    </div>
                                                    <span class="event-teaser__standfirst">Partnerships for success</span>
                                                </div>
                                                <div class="event-teaser__footer">
                                                    <span class="event-teaser__timestamp event-teaser__timestamp--start-date">
                                                        <time dateTime="2023-11-30T09:30:00.000Z">Thursday, 30 November</time>
                                                    </span>
                                                    <span class="event-teaser__location">Teatro Lirico, Via Larga, Milan, Metropolitan City of Milan, Italy</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div data-o-grid-colspan="12 M4 L3" class="community-home-page-slice__column community-home-page-slice__item-column">
                                        <div class="event-teaser" data-trackable="event-teaser" data-trackable-context-content-id="e512158f-ab91-4a75-887b-99f2b192f6b3" data-o-tracking-view="true">
                                            <div class="event-teaser__content-container">
                                                <div class="event-teaser__details">
                                                    <a class="event-teaser__brand" href="https://healthtechsummit.live.ft.com" data-trackable="event-teaser-brand-link">FT Live</a>
                                                    <div class="event-teaser__title-heading" role="heading" aria-level="4">
                                                        <a class="event-teaser__title" data-trackable="event-teaser-title" href="https://healthtechsummit.live.ft.com" title="Health Technology Summit">Health Technology Summit</a>
                                                    </div>
                                                    <span class="event-teaser__standfirst">Powering innovation across health systems</span>
                                                </div>
                                                <div class="event-teaser__footer">
                                                    <span class="event-teaser__timestamp event-teaser__timestamp--start-date">
                                                        <time dateTime="2023-11-30T10:00:00.000Z">Thursday, 30 November</time>
                                                    </span>
                                                    <span class="event-teaser__location">Digital Conference</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="community-home-page-slice o-grid-row o-grid-row--compact community-home-page-slice--forums community-home-page-slice--default-layout">
                                    <div data-o-grid-colspan="12 M12 L3" class="community-home-page-slice__column community-home-page-slice__header-column">
                                        <div class="community-home-page-slice__header">
                                            <div role="heading" aria-level="3" class="community-home-page-slice__title">Join the discussion</div>
                                            <p class="community-home-page-slice__strapline">FT Forums is a series of members only communities, powered by the Financial Times</p>
                                        </div>
                                    </div>
                                    <div data-o-grid-colspan="12 M4 L3" class="community-home-page-slice__column community-home-page-slice__item-column">
                                        <div class="forum-teaser" data-trackable="forum-teaser">
                                            <div role="heading" aria-level="4" class="forum-teaser__title-heading">
                                                <a class="forum-teaser__title" data-trackable="forum-teaser-title" href="https://forums.ft.com/women-in-business-forum">Women In Business Forum</a>
                                            </div>
                                            <span class="forum-teaser__strapline">A dedicated programme to accelerate mid-career women into senior leadership.</span>
                                        </div>
                                    </div>
                                    <div data-o-grid-colspan="12 M4 L3" class="community-home-page-slice__column community-home-page-slice__item-column">
                                        <div class="forum-teaser" data-trackable="forum-teaser">
                                            <div role="heading" aria-level="4" class="forum-teaser__title-heading">
                                                <a class="forum-teaser__title" data-trackable="forum-teaser-title" href="https://forums.ft.com/future-forum">Future Forum</a>
                                            </div>
                                            <span class="forum-teaser__strapline">An authoritative space for businesses to share ideas, build relationships and develop solutions to future challenges.</span>
                                        </div>
                                    </div>
                                    <div data-o-grid-colspan="12 M4 L3" class="community-home-page-slice__column community-home-page-slice__item-column">
                                        <div class="forum-teaser" data-trackable="forum-teaser">
                                            <div role="heading" aria-level="4" class="forum-teaser__title-heading">
                                                <a class="forum-teaser__title" data-trackable="forum-teaser-title" href="https://forums.ft.com/climate-capital-council">Climate Capital Council</a>
                                            </div>
                                            <span class="forum-teaser__strapline">Where businesses share ideas, opportunities and challenges with climate change.</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                    </main>
                </div>
            </div>
            <div class="n-layout__row n-layout__row--footer">
                <div class="n-layout__footer-before">
                    <div class="n-feedback__container n-feedback--hidden"></div>
                </div>
                <footer id="site-footer" class="o-footer o-footer--theme-dark" data-o-component="o-footer">
                    <div class="o-footer__container">
                        <div class="o-footer__row">
                            <h2 class="o-normalise-visually-hidden">Useful links</h2>
                            <nav class="o-footer__matrix" role="navigation" aria-label="Useful links">
                                <div class="o-footer__matrix-group o-footer__matrix-group--1">
                                    <h3 class="o-footer__matrix-title" aria-controls="o-footer-section-0">Support</h3>
                                    <div class="o-footer__matrix-content" id="o-footer-section-0">
                                        <div class="o-footer__matrix-column">
                                            <a class="o-footer__matrix-link" href="/tour" data-trackable="View Site Tips">
                                                <span class="o-footer__matrix-link__copy">View Site Tips</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://help.ft.com" data-trackable="Help Centre">
                                                <span class="o-footer__matrix-link__copy">Help Centre</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://aboutus.ft.com/contact-us" data-trackable="Contact Us">
                                                <span class="o-footer__matrix-link__copy">Contact Us</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://www.ft.com/aboutus" data-trackable="About Us">
                                                <span class="o-footer__matrix-link__copy">About Us</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="/accessibility" data-trackable="Accessibility">
                                                <span class="o-footer__matrix-link__copy">Accessibility</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="/tour/myft" data-trackable="myFT Tour">
                                                <span class="o-footer__matrix-link__copy">myFT Tour</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://aboutus.ft.com/en-gb/careers/" data-trackable="Careers">
                                                <span class="o-footer__matrix-link__copy">Careers</span>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="o-footer__matrix-group o-footer__matrix-group--1">
                                    <h3 class="o-footer__matrix-title" aria-controls="o-footer-section-1">Legal &amp;Privacy</h3>
                                    <div class="o-footer__matrix-content" id="o-footer-section-1">
                                        <div class="o-footer__matrix-column">
                                            <a class="o-footer__matrix-link" href="https://help.ft.com/help/legal-privacy/terms-conditions/" data-trackable="Terms &amp; Conditions">
                                                <span class="o-footer__matrix-link__copy">Terms &amp;Conditions</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://help.ft.com/help/legal-privacy/privacy/" data-trackable="Privacy Policy">
                                                <span class="o-footer__matrix-link__copy">Privacy Policy</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://help.ft.com/help/legal-privacy/cookies/" data-trackable="Cookie Policy">
                                                <span class="o-footer__matrix-link__copy">Cookie Policy</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://www.ft.com/preferences/manage-cookies" data-trackable="Manage Cookies">
                                                <span class="o-footer__matrix-link__copy">Manage Cookies</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://help.ft.com/help/legal-privacy/copyright/copyright-policy/" data-trackable="Copyright">
                                                <span class="o-footer__matrix-link__copy">Copyright</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://help.ft.com/help/legal/slavery-statement/" data-trackable="Slavery Statement &amp; Policies">
                                                <span class="o-footer__matrix-link__copy">Slavery Statement &amp;Policies</span>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="o-footer__matrix-group o-footer__matrix-group--1">
                                    <h3 class="o-footer__matrix-title" aria-controls="o-footer-section-2">Services</h3>
                                    <div class="o-footer__matrix-content" id="o-footer-section-2">
                                        <div class="o-footer__matrix-column">
                                            <a class="o-footer__matrix-link" href="/securedrop" data-trackable="Share News Tips Securely" data-o-tracking-do-not-track="true">
                                                <span class="o-footer__matrix-link__copy">Share News Tips Securely</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://www.ft.com/products" data-trackable="Individual Subscriptions">
                                                <span class="o-footer__matrix-link__copy">Individual Subscriptions</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://professional.ft.com/en-gb/services/professional-subscriptions?segmentId=383c7f[…]4-b62d-cb33-4c278e6fdf61&amp;cpccampaign=B2B_link_ft.com_footer" data-trackable="Professional Subscriptions">
                                                <span class="o-footer__matrix-link__copy">Professional Subscriptions</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://professional.ft.com/en-gb/services/republishing/" data-trackable="Republishing">
                                                <span class="o-footer__matrix-link__copy">Republishing</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://www.exec-appointments.com/" data-trackable="Executive Job Search">
                                                <span class="o-footer__matrix-link__copy">Executive Job Search</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://commercial.ft.com/" data-trackable="Advertise with the FT">
                                                <span class="o-footer__matrix-link__copy">Advertise with the FT</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://twitter.com/ft" data-trackable="Follow the FT on X">
                                                <span class="o-footer__matrix-link__copy">Follow the FT on X</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://channels.ft.com/" data-trackable="FT Channels">
                                                <span class="o-footer__matrix-link__copy">FT Channels</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://enterprise.ft.com/en-gb/services/group-subscriptions/secondary-education/" data-trackable="FT Schools">
                                                <span class="o-footer__matrix-link__copy">FT Schools</span>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="o-footer__matrix-group o-footer__matrix-group--1">
                                    <h3 class="o-footer__matrix-title" aria-controls="o-footer-section-3">Tools</h3>
                                    <div class="o-footer__matrix-content" id="o-footer-section-3">
                                        <div class="o-footer__matrix-column">
                                            <a class="o-footer__matrix-link" href="https://markets.ft.com/data/portfolio/dashboard" data-trackable="Portfolio">
                                                <span class="o-footer__matrix-link__copy">Portfolio</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://www.ft.com/todaysnewspaper" data-trackable="Today’s Newspaper (FT Digital Edition)">
                                                <span class="o-footer__matrix-link__copy">Today’s Newspaper (FT Digital Edition)</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://markets.ft.com/data/alerts/" data-trackable="Alerts Hub">
                                                <span class="o-footer__matrix-link__copy">Alerts Hub</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://rankings.ft.com/" data-trackable="Business School Rankings">
                                                <span class="o-footer__matrix-link__copy">Business School Rankings</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://kat.ft.com/" data-trackable="Enterprise Tools">
                                                <span class="o-footer__matrix-link__copy">Enterprise Tools</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="/news-feed" data-trackable="News feed">
                                                <span class="o-footer__matrix-link__copy">News feed</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="/newsletters" data-trackable="Newsletters">
                                                <span class="o-footer__matrix-link__copy">Newsletters</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://markets.ft.com/data/currencies" data-trackable="Currency Converter">
                                                <span class="o-footer__matrix-link__copy">Currency Converter</span>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="o-footer__matrix-group o-footer__matrix-group--1">
                                    <h3 class="o-footer__matrix-title" aria-controls="o-footer-section-4">Community &amp;Events</h3>
                                    <div class="o-footer__matrix-content" id="o-footer-section-4">
                                        <div class="o-footer__matrix-column">
                                            <a class="o-footer__matrix-link" href="https://www.ft.com/tour/community" data-trackable="FT Community">
                                                <span class="o-footer__matrix-link__copy">FT Community</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://events.ft.com/events-list" data-trackable="FT Live Events">
                                                <span class="o-footer__matrix-link__copy">FT Live Events</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://forums.ft.com/" data-trackable="FT Forums">
                                                <span class="o-footer__matrix-link__copy">FT Forums</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://enterprise.ft.com/board-director-membership" data-trackable="FT Board Director">
                                                <span class="o-footer__matrix-link__copy">FT Board Director</span>
                                            </a>
                                            <a class="o-footer__matrix-link" href="https://bdp.ft.com/" data-trackable="Board Director Programme">
                                                <span class="o-footer__matrix-link__copy">Board Director Programme</span>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="o-footer__matrix-group o-footer__matrix-group--1">
                                    <h3 class="o-footer__matrix-title o-footer__matrix-title--link">
                                        <a class="o-footer__matrix-link o-footer__matrix-link--more" id="o-footer-5" href="https://ft.com/more-from-ft-group">
                                            <span class="o-footer__matrix-link__copy">More from the FT Group</span>
                                        </a>
                                    </h3>
                                </div>
                            </nav>
                        </div>
                        <div class="o-footer__copyright">
                            <small>
                                Markets data delayed by at least 15 minutes. © THE FINANCIAL TIMES LTD 2023. <abbr title="Financial Times" aria-label="F T">FT</abbr>
                                and ‘Financial Times’ are trademarks of The Financial Times Ltd.<br/>
                                The Financial Times and its journalism are subject to a self-regulation regime under the <a href="https://aboutus.ft.com/en-gb/ft-editorial-code/" aria-label="F T Editorial Code of Practice">FT Editorial Code of Practice</a>
                                .
                            </small>
                        </div>
                    </div>
                    <div class="o-footer__brand">
                        <div class="o-footer__container">
                            <div class="o-footer__brand-logo"></div>
                        </div>
                    </div>
                </footer>
                <div class="n-layout__footer-after">
                    <script data-pixel-src="https://spoor-api.ft.com/px.gif?data=%7B%22category%22%3A%22page%22%2C%22action%22%3A%22view%22%2C%22system%22%3A%7B%22source%22%3A%22non-ctm%22%7D%2C%22context%22%3A%7B%22name%22%3A%22home-page%22%2C%22product%22%3A%22next%22%2C%22data%22%3A%7B%22source%22%3A%22%5BSOURCE%5D%22%7D%7D%7D">
                        (function coreExperience() {
                            if (/\bcore\b/.test(document.documentElement.className)) {
                                var currentScript = document.scripts[document.scripts.length - 1];
                                var img = new Image();
                                img.src = currentScript.getAttribute('data-pixel-src');
                            }
                        }
                        )();
                    </script>
                    <noscript>
                        <img src="https://spoor-api.ft.com/px.gif?data=%7B%22category%22%3A%22page%22%2C%22action%22%3A%22view%22%2C%22system%22%3A%7B%22source%22%3A%22non-ctm%22%7D%2C%22context%22%3A%7B%22name%22%3A%22home-page%22%2C%22product%22%3A%22next%22%2C%22data%22%3A%7B%22source%22%3A%22%5BSOURCE%5D%22%7D%7D%7D" alt=""/>
                    </noscript>
                </div>
            </div>
            <div class="o-header__drawer" id="o-header-drawer" role="modal" aria-label="Drawer menu" aria-modal="true" data-o-header-drawer="true" data-o-header-drawer--no-js="true" data-trackable="drawer" data-trackable-terminate="true">
                <div class="o-header__drawer-inner">
                    <div class="o-header__drawer-tools">
                        <button type="button" class="o-header__drawer-tools-close" title="Close side navigation menu" aria-controls="o-header-drawer" data-trackable="close">
                            <span class="o-header__visually-hidden">Close side navigation menu</span>
                        </button>
                        <a class="o-header__drawer-tools-logo" href="/" data-trackable="logo">
                            <span class="o-header__visually-hidden">Financial Times</span>
                        </a>
                        <p class="o-header__drawer-current-edition">UK Edition</p>
                    </div>
                    <div class="o-header__drawer-actions">
                        <a class="o-header__drawer-button" role="button" href="/products?segmentId=4526c036-7527-ab37-9a29-0b0403fa0b5f" data-trackable="subscribe-button">Subscribe for full access</a>
                    </div>
                    <div class="o-header__drawer-search">
                        <form class="o-header__drawer-search-form" action="/search" role="search" aria-label="Site search" data-n-topic-search="true" data-n-topic-search-categories="concepts,equities" data-n-topic-search-view-all="true">
                            <label class="o-header__visually-hidden" for="o-header-drawer-search-term">
                                Search the <abbr title="Financial Times">FT</abbr>
                            </label>
                            <input type="text" class="o-header__drawer-search-term" id="o-header-drawer-search-term" name="q" autoComplete="off" autoCorrect="off" autoCapitalize="off" spellcheck="false" placeholder="Search the FT" data-trackable="search-term" data-n-topic-search-input="true"/>
                            <button class="o-header__drawer-search-submit" type="submit" data-trackable="search-submit">
                                <span class="o-header__visually-hidden">Search</span>
                            </button>
                        </form>
                    </div>
                    <nav class="o-header__drawer-menu" aria-label="Edition switcher">
                        <ul class="o-header__drawer-menu-list">
                            <li class="o-header__drawer-menu-item" data-trackable="edition-switcher">
                                <a class="o-header__drawer-menu-link" href="/?edition=international" data-trackable="international">Switch to International Edition</a>
                            </li>
                        </ul>
                    </nav>
                    <nav class="o-header__drawer-menu o-header__drawer-menu--primary">
                        <h2 id="top-sections" class="o-header__drawer-menu-item o-header__drawer-menu-item--heading">Top sections</h2>
                        <ul aria-labelledby="top-sections" class="o-header__drawer-menu-list">
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--selected" href="/" data-trackable="Home" aria-label="Home, current page" aria-current="page">Home</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <div class="o-header__drawer-menu-toggle-wrapper">
                                    <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--parent" href="/world" data-trackable="World">World</a>
                                    <button class="o-header__drawer-menu-toggle o-header__drawer-menu-toggle--unselected" aria-controls="o-header-drawer-child-1" data-trackable="sub-level-toggle | World">Show more World</button>
                                </div>
                                <ul class="o-header__drawer-menu-list o-header__drawer-menu-list--child" id="o-header-drawer-child-1" data-trackable="sub-level">
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/israel-hamas-war" data-trackable="Israel-Hamas war">Israel-Hamas war</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/global-economy" data-trackable="Global Economy">Global Economy</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/world-uk" data-trackable="UK">UK</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/us" data-trackable="US">US</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/china" data-trackable="China">China</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/africa" data-trackable="Africa">Africa</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/asia-pacific" data-trackable="Asia Pacific">Asia Pacific</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/emerging-markets" data-trackable="Emerging Markets">Emerging Markets</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/europe" data-trackable="Europe">Europe</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/war-in-ukraine" data-trackable="War in Ukraine">War in Ukraine</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/americas" data-trackable="Americas">Americas</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/middle-east-north-africa" data-trackable="Middle East &amp; North Africa">Middle East &amp;North Africa</a>
                                    </li>
                                </ul>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <div class="o-header__drawer-menu-toggle-wrapper">
                                    <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--parent" href="/world-uk" data-trackable="UK">UK</a>
                                    <button class="o-header__drawer-menu-toggle o-header__drawer-menu-toggle--unselected" aria-controls="o-header-drawer-child-2" data-trackable="sub-level-toggle | UK">Show more UK</button>
                                </div>
                                <ul class="o-header__drawer-menu-list o-header__drawer-menu-list--child" id="o-header-drawer-child-2" data-trackable="sub-level">
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/uk-economy" data-trackable="UK Economy">UK Economy</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/uk-politics" data-trackable="UK Politics">UK Politics</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/brexit" data-trackable="Brexit">Brexit</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/uk-companies" data-trackable="UK Companies">UK Companies</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/personal-finance" data-trackable="Personal Finance">Personal Finance</a>
                                    </li>
                                </ul>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <div class="o-header__drawer-menu-toggle-wrapper">
                                    <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--parent" href="/companies" data-trackable="Companies">Companies</a>
                                    <button class="o-header__drawer-menu-toggle o-header__drawer-menu-toggle--unselected" aria-controls="o-header-drawer-child-3" data-trackable="sub-level-toggle | Companies">Show more Companies</button>
                                </div>
                                <ul class="o-header__drawer-menu-list o-header__drawer-menu-list--child" id="o-header-drawer-child-3" data-trackable="sub-level">
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/energy" data-trackable="Energy">Energy</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/financials" data-trackable="Financials">Financials</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/health" data-trackable="Health">Health</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/industrials" data-trackable="Industrials">Industrials</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/media" data-trackable="Media">Media</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/professional-services" data-trackable="Professional Services">Professional Services</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/retail-consumer" data-trackable="Retail &amp; Consumer">Retail &amp;Consumer</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/technology-sector" data-trackable="Tech Sector">Tech Sector</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/telecoms" data-trackable="Telecoms">Telecoms</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/transport" data-trackable="Transport">Transport</a>
                                    </li>
                                </ul>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <div class="o-header__drawer-menu-toggle-wrapper">
                                    <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--parent" href="/technology" data-trackable="Tech">Tech</a>
                                    <button class="o-header__drawer-menu-toggle o-header__drawer-menu-toggle--unselected" aria-controls="o-header-drawer-child-4" data-trackable="sub-level-toggle | Tech">Show more Tech</button>
                                </div>
                                <ul class="o-header__drawer-menu-list o-header__drawer-menu-list--child" id="o-header-drawer-child-4" data-trackable="sub-level">
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/artificial-intelligence" data-trackable="Artificial intelligence">Artificial intelligence</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/semiconductors" data-trackable="Semiconductors">Semiconductors</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/cyber-security" data-trackable="Cyber Security">Cyber Security</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/social-media" data-trackable="Social Media">Social Media</a>
                                    </li>
                                </ul>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <div class="o-header__drawer-menu-toggle-wrapper">
                                    <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--parent" href="/markets" data-trackable="Markets">Markets</a>
                                    <button class="o-header__drawer-menu-toggle o-header__drawer-menu-toggle--unselected" aria-controls="o-header-drawer-child-5" data-trackable="sub-level-toggle | Markets">Show more Markets</button>
                                </div>
                                <ul class="o-header__drawer-menu-list o-header__drawer-menu-list--child" id="o-header-drawer-child-5" data-trackable="sub-level">
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/alphaville" data-trackable="Alphaville">Alphaville</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="https://markets.ft.com/data" data-trackable="Markets Data">Markets Data</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/cryptofinance" data-trackable="Cryptofinance">Cryptofinance</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/capital-markets" data-trackable="Capital Markets">Capital Markets</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/commodities" data-trackable="Commodities">Commodities</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/currencies" data-trackable="Currencies">Currencies</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/equities" data-trackable="Equities">Equities</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/fund-management" data-trackable="Fund Management">Fund Management</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/ft-wealth-management" data-trackable="Wealth Management">Wealth Management</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/ft-trading-room" data-trackable="Trading">Trading</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/moral-money" data-trackable="Moral Money">Moral Money</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="https://etf.ft.com" data-trackable="ETF Hub">ETF Hub</a>
                                    </li>
                                </ul>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/climate-capital" data-trackable="Climate">Climate</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <div class="o-header__drawer-menu-toggle-wrapper">
                                    <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--parent" href="/opinion" data-trackable="Opinion">Opinion</a>
                                    <button class="o-header__drawer-menu-toggle o-header__drawer-menu-toggle--unselected" aria-controls="o-header-drawer-child-7" data-trackable="sub-level-toggle | Opinion">Show more Opinion</button>
                                </div>
                                <ul class="o-header__drawer-menu-list o-header__drawer-menu-list--child" id="o-header-drawer-child-7" data-trackable="sub-level">
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/columnists" data-trackable="Columnists">Columnists</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/ft-view" data-trackable="The FT View">The FT View</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/lex" data-trackable="Lex">Lex</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/obituaries" data-trackable="Obituaries">Obituaries</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/letters" data-trackable="Letters">Letters</a>
                                    </li>
                                </ul>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <div class="o-header__drawer-menu-toggle-wrapper">
                                    <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--parent" href="/work-careers" data-trackable="Work &amp; Careers">Work &amp;Careers</a>
                                    <button class="o-header__drawer-menu-toggle o-header__drawer-menu-toggle--unselected" aria-controls="o-header-drawer-child-8" data-trackable="sub-level-toggle | Work &amp; Careers">Show more Work &amp;Careers</button>
                                </div>
                                <ul class="o-header__drawer-menu-list o-header__drawer-menu-list--child" id="o-header-drawer-child-8" data-trackable="sub-level">
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="https://rankings.ft.com/" data-trackable="Business School Rankings">Business School Rankings</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/business-education" data-trackable="Business Education">Business Education</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/entrepreneurship" data-trackable="Entrepreneurship">Entrepreneurship</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/recruitment" data-trackable="Recruitment">Recruitment</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/business-books" data-trackable="Business Books">Business Books</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/business-travel" data-trackable="Business Travel">Business Travel</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/working-it" data-trackable="Working It">Working It</a>
                                    </li>
                                </ul>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <div class="o-header__drawer-menu-toggle-wrapper">
                                    <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--parent" href="/life-arts" data-trackable="Life &amp; Arts">Life &amp;Arts</a>
                                    <button class="o-header__drawer-menu-toggle o-header__drawer-menu-toggle--unselected" aria-controls="o-header-drawer-child-9" data-trackable="sub-level-toggle | Life &amp; Arts">Show more Life &amp;Arts</button>
                                </div>
                                <ul class="o-header__drawer-menu-list o-header__drawer-menu-list--child" id="o-header-drawer-child-9" data-trackable="sub-level">
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/arts" data-trackable="Arts">Arts</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/books" data-trackable="Books">Books</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/food-drink" data-trackable="Food &amp; Drink">Food &amp;Drink</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/magazine" data-trackable="FT Magazine">FT Magazine</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/house-home" data-trackable="House &amp; Home">House &amp;Home</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/style" data-trackable="Style">Style</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/travel" data-trackable="Travel">Travel</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/globetrotter" data-trackable="FT Globetrotter">FT Globetrotter</a>
                                    </li>
                                </ul>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <div class="o-header__drawer-menu-toggle-wrapper">
                                    <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--parent" href="/personal-finance" data-trackable="Personal Finance">Personal Finance</a>
                                    <button class="o-header__drawer-menu-toggle o-header__drawer-menu-toggle--unselected" aria-controls="o-header-drawer-child-10" data-trackable="sub-level-toggle | Personal Finance">Show more Personal Finance</button>
                                </div>
                                <ul class="o-header__drawer-menu-list o-header__drawer-menu-list--child" id="o-header-drawer-child-10" data-trackable="sub-level">
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/mortgages" data-trackable="Property &amp; Mortgages">Property &amp;Mortgages</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/investments" data-trackable="Investments">Investments</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/pensions" data-trackable="Pensions">Pensions</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/tax" data-trackable="Tax">Tax</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/banking-savings" data-trackable="Banking &amp; Savings">Banking &amp;Savings</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/advice-comment" data-trackable="Advice &amp; Comment">Advice &amp;Comment</a>
                                    </li>
                                    <li class="o-header__drawer-menu-item">
                                        <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--child" href="/next-act" data-trackable="Next Act">Next Act</a>
                                    </li>
                                </ul>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/htsi" data-trackable="HTSI">HTSI</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/special-reports" data-trackable="Special Reports">Special Reports</a>
                            </li>
                        </ul>
                        <h2 id="ft-recommends" class="o-header__drawer-menu-item o-header__drawer-menu-item--heading">FT recommends</h2>
                        <ul aria-labelledby="ft-recommends" class="o-header__drawer-menu-list">
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/lex" data-trackable="Lex">Lex</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/alphaville" data-trackable="Alphaville">Alphaville</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/lunch-with-the-ft" data-trackable="Lunch with the FT">Lunch with the FT</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/globetrotter" data-trackable="FT Globetrotter">FT Globetrotter</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="https://www.ft.com/tech-asia" data-trackable="#techAsia">#techAsia</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/moral-money" data-trackable="Moral Money">Moral Money</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/visual-and-data-journalism" data-trackable="Visual and data journalism">Visual and data journalism</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/newsletters" data-trackable="Newsletters">Newsletters</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/video" data-trackable="Video">Video</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="https://www.ft.com/podcasts" data-trackable="Podcasts">Podcasts</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="/news-feed" data-trackable="News feed">News feed</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="https://events.ft.com/events-list" data-trackable="FT Live Events">FT Live Events</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="https://forums.ft.com/" data-trackable="FT Forums">FT Forums</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected" href="https://bdp.ft.com/" data-trackable="Board Director Programme">Board Director Programme</a>
                            </li>
                        </ul>
                        <ul class="o-header__drawer-menu-list o-header__drawer-menu-list--divide">
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--secondary" href="/myft" data-trackable="myFT">myFT</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--secondary" href="https://markets.ft.com/data/portfolio/dashboard" data-trackable="Portfolio">Portfolio</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--secondary" href="https://www.ft.com/todaysnewspaper" data-trackable="Today’s Newspaper (FT Digital Edition)">Today’s Newspaper (FT Digital Edition)</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--secondary" href="https://www.ft.com/crossword" data-trackable="Crossword">Crossword</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link o-header__drawer-menu-link--unselected o-header__drawer-menu-link--secondary" href="https://www.ft.com/tour/apps" data-trackable="Our Apps">Our Apps</a>
                            </li>
                        </ul>
                    </nav>
                    <nav class="o-header__drawer-menu o-header__drawer-menu--user" data-trackable="user-nav">
                        <ul class="o-header__drawer-menu-list">
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link" href="https://help.ft.com" data-trackable="Help Centre">Help Centre</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link" href="/products?segmentId=d290332b-e8e8-d29b-2ff4-2019b13f008a" data-trackable="Subscribe">Subscribe</a>
                            </li>
                            <li class="o-header__drawer-menu-item">
                                <a class="o-header__drawer-menu-link" href="/login?location=/" data-trackable="Sign In">Sign In</a>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
        </div>
        <script type="application/json" id="page-kit-app-context">
            {
                "appName": "home-page",
                "product": "next",
                "edition": "uk",
                "appVersion": "5b3e8c515a000df7f5efe80c85b25a710d74c1f8",
                "abTestState": "messageSlotBottom:cookieConsentC,chartbeat:variant,optimizelyHomePage:variant,articlecommunitypromoevent:variant2",
                "isProduction": true,
                "isUserLoggedIn": false,
                "pageKitVersion": "8.2.3"
            }</script>
        <script type="application/json" id="page-kit-flags-embed">
            {
                "articleRelatedContent": true,
                "ads": true,
                "javascript": true,
                "oTracking": true,
                "articleComments": true,
                "myFtApi": true,
                "articleShareButtons": true,
                "myFtApiWrite": true,
                "adTargetingUserApi": true,
                "videoPlayerAdvertising": true,
                "streamMostRead": true,
                "serviceWorker": true,
                "openGraph": true,
                "nativeAds": true,
                "myFtDigestPromo": true,
                "regionalNews": true,
                "syndication": true,
                "myFTEmailDisableABAlloc": true,
                "streamRecommendedStoriesList": true,
                "swAssetCaching": true,
                "refererCohort": true,
                "newsletterSignupOnArticle": true,
                "myFTInstantNotifications": true,
                "myftPrioritiseTopics": true,
                "myftIndustryRecs": true,
                "qualtrics": true,
                "showEventPromo": true,
                "myftConsentSwitch": true,
                "moatAdsTraffic": true,
                "manageCookiesWhiteLabel": true,
                "myftIndustryRecsFeed": true,
                "AdsPermutive": true,
                "syndication_promo": true,
                "messageSlotBottom": "cookieConsentC",
                "enableGTM": true,
                "myftNewNewLabel": true,
                "myftBoldNewArticles": true,
                "myftPageAppNotificationsToggle": true,
                "realUserMonitoringForPerformance": true,
                "textCopyTracking": true,
                "enableIHSindexBasedTargetingScript": true,
                "enableBrandmetricsSurveyScript": true,
                "managePremiumCancellationJourney": true,
                "articleInstantAlertsPromo": true,
                "manageStepUpCancellationJourney": true,
                "manageStandardCancellationJourney": true,
                "manageStepUpTransitionJourney": true,
                "manageDirectCancellationJourney": true,
                "privShowCCPALinkOnFooter": true,
                "optimizely": true,
                "accountSettingsBillingDetailsPaypal": true,
                "graphicSyndication": true,
                "adsNativeLazyload": true,
                "adsMoatTimeout": true,
                "enableRavelinOnProd": true,
                "enableMarketingAnalyticsTags": true,
                "streamPageGraphicsList": true,
                "useFlourish": true,
                "adsHighImpact": true,
                "monthlyTermForPremiumCovidCohort": true,
                "enableNonUKDeliveryAddress": true,
                "homePageHeaderMarketsData": true,
                "enableGoogleExtendedMeter": true,
                "communityLandingPage": true,
                "inArticleContentSignUp": true,
                "frontPageCommunitySection": true,
                "newBuyFlow": true,
                "bizzaboRegistrationEnabled": true,
                "enableSingleTermSubscriptions": true,
                "newsletterAutoEnrolment": true,
                "eventsInMyFtPage": true,
                "eventsInDigestEmails": true,
                "eventsInStreamPage": true,
                "newslettersRedesign": true,
                "ftGlobetrotterBanner": true,
                "scrollytellingImages": true,
                "chartbeat": "variant",
                "newImageQualityTransform": true,
                "exponeaOnNextArticle": true,
                "emailVerificationOnSignupForms": true,
                "AdsExtraMobileSlot": true,
                "showTheEditAppButton": true,
                "dotcomPages": true,
                "fomoPage": true,
                "enterpriseWorkspaceOnboarding": true,
                "exponeaOnsiteMessaging": true,
                "contentPipelineNextArticle": true,
                "homepageInteractivesEmbeds": true,
                "contentPipelineNextArticlePerformanceTest": true,
                "articleTrialTemplate": true,
                "bankTransferFeature": true,
                "optimizelyHomePage": "variant",
                "articlecommunitypromoevent": "variant2",
                "purgeableLongTailArticleCaching": true,
                "myAccountLanding": true,
                "chatterboxChat": true,
                "liveChat": true,
                "billingDetailsConfirmationPage": true,
                "graphQLMigrationUseGQLData": true,
                "AdsCompaniesTypeaheadDemo": true,
                "enterpriseUserAnnotations": true,
                "reverseCancellation": true,
                "useZephrDecision": true,
                "adsPGHomePage": true,
                "saveMeDisplayEdit": true,
                "adsPGSearchPage": true,
                "stripeForIndia": true,
                "useGoogleExtendedAccessNewAPI": true,
                "showNoOffersPageInRetention": true,
                "makeSubsGraphQlQuery": true,
                "retentionGetTrabsitionData": true,
                "myFTInstantAlertsOnboarding": true,
                "proCentralBanking": true,
                "magnetOnArticle": true,
                "myftFollowButton": true,
                "removeProfileRoute": true,
                "centralBankingBannerWorkspace": true
            }</script>
    </body>
</html>
"""