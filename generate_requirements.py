import ast

def get_install_requires():
    with open('setup.py', 'r') as f:
        setup_contents = f.read()
    
    tree = ast.parse(setup_contents)
    install_requires = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, 'id', '') == 'setup':
            for keyword in node.keywords:
                if keyword.arg == 'install_requires':
                    install_requires = [elt.s for elt in keyword.value.elts]
                    break
    
    return install_requires

def write_requirements_file(requirements):
    with open('requirements.txt', 'w') as f:
        for requirement in requirements:
            f.write(requirement + '\n')

if __name__ == '__main__':
    install_requires = get_install_requires()
    if install_requires:
        write_requirements_file(install_requires)
        print('requirements.txt generated successfully.')
    else:
        print('No install_requires found in setup.py.')
