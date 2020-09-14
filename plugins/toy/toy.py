#
# 《The missing Pelican plugins guide》
#  Published January 11, 2020 • 10 minutes read
#  https://blog.geographer.fr/pelican-plugins
#

from pelican import signals

# Hook function, with the right parameters
def run(path, context):
    print("By toy plugin: " + path)


# Module entry point
def register():
    # Connect the run hook function to the content_written signal
    signals.content_written.connect(run)
