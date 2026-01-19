import re

class NavigationService:
    """
    Serviço centralizado para cálculo de navegação linear entre lições.
    Extraído de build/fases/*.py para obediência ao DRY.
    """
    
    @staticmethod
    def _generate_filename(lid, titulo):
        """
        Gera nome do arquivo IDÊNTICO ao GutenbergEngine (Core).
        Lógica: UPPERCASE + Underscores + Apenas Alphanum.
        """
        clean_title = str(titulo).replace(' ', '_').upper()
        # Filtro alnum idêntico ao engine.py
        clean_title = "".join([c for c in clean_title if c.isalnum() or c in ('_', '-')])
        return f"{lid}_{clean_title}.html"

    @staticmethod
    def calculate_links(lessons_data):
        """
        Recebe lista de lições (formato Engine: {'data': ..., 'id': ...}).
        Retorna a mesma lista com 'prev_licao' e 'next_licao' injetados.
        """
        # 1. Ordenar por ID da lição
        sorted_lessons = sorted(
            lessons_data, 
            key=lambda x: x['data']['licao']['metadados']['id']
        )
        
        # 2. Injetar Vizinhos
        for i, item in enumerate(sorted_lessons):
            current_yaml = item['data']['licao']
            
            # Anterior
            if i > 0:
                prev = sorted_lessons[i-1]['data']['licao']['metadados']
                filename = NavigationService._generate_filename(prev['id'], prev['titulo'])
                
                # Injeta dado estruturado para Template
                item['prev_licao'] = {
                    'titulo': prev['titulo'],
                    'url': filename
                }
                # Fallback manual no YAML
                if 'navegacao' not in current_yaml: current_yaml['navegacao'] = {}
                current_yaml['navegacao']['anterior'] = {
                    'id': prev['id'], 
                    'titulo': prev['titulo'],
                    'url': filename
                }

            # Próximo
            if i < len(sorted_lessons) - 1:
                nxt = sorted_lessons[i+1]['data']['licao']['metadados']
                filename = NavigationService._generate_filename(nxt['id'], nxt['titulo'])
                
                item['next_licao'] = {
                    'titulo': nxt['titulo'],
                    'url': filename
                }
                # Fallback manual no YAML
                if 'navegacao' not in current_yaml: current_yaml['navegacao'] = {}
                current_yaml['navegacao']['proxima'] = {
                    'id': nxt['id'], 
                    'titulo': nxt['titulo'],
                    'url': filename
                }
                
        return sorted_lessons
