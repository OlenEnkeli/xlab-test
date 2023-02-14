import sys
import logging.config

from argparse import ArgumentParser

import coloredlogs

from peewee_migrate import Router

from app.core.db.manager import db, manager
from app.core.settings import LOG_CONFIG


coloredlogs.install()
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)


def router_action(action, error_message, name=None):
    try:
        action(name)
    except Exception as e:
        logger.error(error_message)
        logger.error(e)
        sys.exit(1)


router = Router(db)

parser = ArgumentParser(description='Peewee migration wrapper')

parser.add_argument(
    'action',
    metavar='action',
    type=str,
    help='migrate / create',
)
parser.add_argument(
    'name',
    default=None,
    metavar='migration name',
    type=str,
)

args = parser.parse_args()

with manager.allow_sync():
    if not (args.name and args.action):
        ArgumentParser.error()

    if args.action == 'create':
        router_action(router.create, 'Can`t create migration "{args.name}"', args.name)

    elif args.action == 'migrate':
        if args.name == 'all':
            router_action(router.run, 'Can`t apply migrations')
        else:
            router_action(router.run, 'Can`t apply migration "{args.name}"', args.name)

    else:
        ArgumentParser.error()
