#!/bin/bash
###############################################################################

DD_APM_ENABLED=${DD_APM_ENABLED:-FALSE}

###############################################################################

ACTION=""
if [ $# -ge 1 ]; then
  ACTION=${1} ; shift
fi

DD_TRACE_BIN=""
[[ "${DD_APM_ENABLED^^}" == "TRUE" ]] && DD_TRACE_BIN=ddtrace-run

case "${ACTION}" in

  ''|-*)
    sleep 0.5
    exec ${DD_TRACE_BIN} uvicorn ${UVICORN_APP} ${ACTION} ${@}
    ;;

  uvicorn)
    sleep 0.5
    exec ${DD_TRACE_BIN} uvicorn ${UVICORN_APP} ${@}
    ;;

  *)
    exec ${ACTION} ${@}
    ;;

esac
