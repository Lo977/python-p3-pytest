U
    ��f2  �                   @   s&   d dl Zd dlm  mZ dd� ZdS )�    Nc                 C   sX   | j j}| j}|jr|j�� n|jj}|jr6|j�� n|j}|sD|rTd�||f�| _d S )N� )�parent�obj�__doc__�strip�	__class__�__name__�join�_nodeid)�itemZpar�nodeZpref�suf� r   �Q/Users/buddhalo/Development/code/phase-3/python-p3-pytest/lib/testing/conftest.py�pytest_itemcollected   s    r   )�builtins�@py_builtins�_pytest.assertion.rewrite�	assertion�rewrite�
@pytest_arr   r   r   r   r   �<module>   s     