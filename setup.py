from setuptools import setup, find_packages
    
    with open('README.md', encoding='utf-8') as f: # README.md 내용 읽어오기
        long_description = f.read()
    
    setup(
        name                = 'weight2cpp',
        version             = '0.1', # PyPI에 올릴 version 
        long_description    = long_description, # README.md 내용을 PyPI project Description에 넣기
        long_description_content_type = 'text/markdown', # 형식은 markdown으로 지정
        description         = 'from AI weight to cpp array', # 짦은 소개
        author              = 'eunju Kim', # 이름
        author_email        = 'ejkim@kisti.re.kr', # 메일 
        url                 = 'https://github.com/ejkim-kr/weight2cpp', # github url
        download_url        = 'https://github.com/ejkim-kr/weight2cpp/archive/weight2cpp_v0.1.zip', # release 이름
        install_requires    =  ["numpy"], # 패키지 사용시 필요한 모듈
        packages            = find_packages(exclude = []),
        keywords            = ['weight','cpp', 'array'], # 키워드
        python_requires     = '>=3.6', # python 필요 버전
        package_data        = {}, 
        zip_safe            = False,
        classifiers         = [   
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )
