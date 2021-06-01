from controller.Neo4jController import Neo4jController
from controller.Controller import Controller, Tags
from servers.Neo4jServer import Neo4jServer

menu_list = {
    'Neo4j menu': {
        'Tagged messages': Neo4jController.get_users_with_tagged_messages,
        'N long relations': Neo4jController.get_users_with_n_long_relations,
        'Shortest way': Neo4jController.shortest_way_between_users,
        'Only spam conversation': Neo4jController.get_users_wicth_have_only_spam_conversation,
        'Tagged messages without relations': Neo4jController.get_unrelated_users_with_tagged_messages,
        'Exit': Controller.stop_loop,
    }
}

roles = {
    'utilizer': 'Utilizer menu',
    'admin': 'Admin menu'
}

neo4j = Neo4jServer()
special_parameters = {
    'role': '(admin or utilizer)',
    'tags': '('+', '.join(x.name for x in list(Tags))+')(Enter comma-separated values)',
    'username1': '(' + ', '.join(x for x in neo4j.get_users()) + ')',
    'username2': '(' + ', '.join(x for x in neo4j.get_users()) + ')'
}
