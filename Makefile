ifeq ($(MAKECMDGOALS),me a sandwich)
.PHONY :: me a sandwich
me a:
	@:

sandwich:
	@[ `id -u` -ne 0 ] && echo "What? Make it yourself." || echo Okay.
endif
