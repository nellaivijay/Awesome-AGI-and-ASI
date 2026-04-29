# Data Pipeline Contribution Guide

This guide explains how the Awesome-AGI-and-ASI DataPipeline integrates with the main repository and how you can contribute to improving the automated resource discovery and enrichment system.

## Overview

The DataPipeline is a self-hosted control plane that:
1. **Fetches** new AGI/ASI resources from multiple sources (arXiv, GitHub, HuggingFace, OpenReview, RSS)
2. **Enriches** each resource via local LLM (Gemma 4 via LM Studio)
3. **Deduplicates** against existing data files
4. **Submits** PRs to the main repository with new YAML entries

## Architecture Integration

```
DataPipeline (Private) → PR Submissions → Awesome-AGI-and-ASI (Public)
     ↓                                          ↓
Local LLM Enrichment                      data/*.yaml files
     ↓                                          ↓
Quality Checks                          Documentation Generation
     ↓                                          ↓
Automated Testing                       MkDocs Site Build
```

## Data Structure

### YAML File Format
Each data file in `data/` follows this structure:

```yaml
section:
  title: Section Name
  description: Section description
  badges:
    - alt: Badge Name
      path: badge-url
subsections:
- title: Subsection Name
  type: paper|tool|framework|resource
  level: 3
  columns:
  - Column Name
  items:
  - name: Resource Name
    author: Author/Org
    year: Year
    description: Description
    links:
      - type: Link Type
        url: URL
```

### Data Files Mapping

| Pipeline Source | Target Data File | Content Type |
|----------------|------------------|--------------|
| arXiv | `data/papers-blogs.yaml` | Research papers |
| GitHub | `data/frameworks.yaml`, `data/agents.yaml` | Tools and frameworks |
| HuggingFace | `data/papers-blogs.yaml`, `data/frameworks.yaml` | Models and papers |
| OpenReview | `data/papers-blogs.yaml` | Conference papers |
| RSS | `data/papers-blogs.yaml` | Blog posts and releases |

## Enhancement Process

### 1. Fetching
Each fetcher monitors its source for new content:
- **arXiv**: Daily fetch of cs.AI, cs.LG, cs.CL, cs.MA
- **GitHub**: Weekly scan for trending AGI/ASI repositories
- **HuggingFace**: Daily check for new models and papers
- **OpenReview**: Conference submission tracking
- **RSS**: Blog post aggregation from major AI labs

### 2. Enrichment
Local LLM (Gemma 4) processes each fetched item:
```python
# Example enrichment process
def enrich_item(item):
    # Summarize
    summary = llm.summarize(item.content)
    
    # Categorize
    category = llm.categorize(item.content, categories=AGI_CATEGORIES)
    
    # Extract key information
    key_info = llm.extract_info(item.content, fields=REQUIRED_FIELDS)
    
    # Generate description
    description = llm.generate_description(item.content, style=REPOSITORY_STYLE)
    
    return enriched_item
```

### 3. Deduplication
Fuzzy matching against existing entries:
```python
def is_duplicate(new_item, existing_items):
    for existing in existing_items:
        similarity = fuzzy_match(new_item.name, existing.name)
        if similarity > 0.85:  # 85% similarity threshold
            return True
    return False
```

### 4. PR Submission
Automated PR creation with:
- Descriptive title: "Add [source_type] resources from [date]"
- Detailed description of changes
- Proper YAML formatting
- Category and subsection organization

## Configuration

### Pipeline Configuration
Edit `config/pipeline.yaml`:

```yaml
sources:
  arxiv:
    enabled: true
    categories:
      - cs.AI
      - cs.LG
      - cs.CL
      - cs.MA
    days_to_fetch: 7
    
  github:
    enabled: true
    topics:
      - agi
      - llm-agents
      - ai-agents
      - artificial-general-intelligence
    min_stars: 100
    
  huggingface:
    enabled: true
    model_types:
      - text-generation
      - code-generation
      - multimodal
    min_downloads: 1000

enrichment:
  model: gemma-4
  endpoint: http://localhost:1234
  max_tokens: 500
  temperature: 0.7

deduplication:
  similarity_threshold: 0.85
  check_fields:
    - name
    - author
    - url

submission:
  target_repo: nellaivijay/Awesome-AGI-and-ASI
  branch_prefix: data-pipeline/
  auto_merge: false
```

## Quality Checks

### Automated Validation
Each enriched item passes through quality checks:

```python
def validate_enriched_item(item):
    # Required fields
    assert item.name, "Name is required"
    assert item.description, "Description is required"
    assert item.links, "At least one link is required"
    
    # Content quality
    assert len(item.description) > 50, "Description too short"
    assert len(item.description) < 500, "Description too long"
    
    # Relevance check
    relevance = llm.check_relevance(item.content, AGI_KEYWORDS)
    assert relevance > 0.7, "Item not relevant to AGI/ASI"
    
    # Freshness check
    if item.year:
        assert item.year >= 2024, "Item too old"
    
    return True
```

### Manual Review Process
1. Pipeline submits PR with enriched items
2. Maintainer reviews for:
   - Accuracy of categorization
   - Quality of descriptions
   - Relevance to AGI/ASI
   - Proper formatting
3. Maintainer can:
   - Approve and merge
   - Request changes via PR comments
   - Reject individual items while accepting others

## Extending the Pipeline

### Adding New Fetchers

1. Create new fetcher in `pipeline/fetchers/`:

```python
# pipeline/fetchers/custom_source.py
from typing import List, Dict, Any
from ..base_fetcher import BaseFetcher

class CustomSourceFetcher(BaseFetcher):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.api_endpoint = config.get('api_endpoint')
        self.api_key = config.get('api_key')
    
    def fetch(self) -> List[Dict[str, Any]]:
        """Fetch items from custom source"""
        # Implementation
        pass
    
    def parse(self, raw_data: Any) -> List[Dict[str, Any]]:
        """Parse raw data into standard format"""
        # Implementation
        pass
```

2. Register in `pipeline/config.py`:

```python
FETCHER_REGISTRY = {
    'arxiv': ArXivFetcher,
    'github': GitHubFetcher,
    'huggingface': HuggingFaceFetcher,
    'openreview': OpenReviewFetcher,
    'rss': RSSFetcher,
    'custom_source': CustomSourceFetcher,  # New fetcher
}
```

3. Add configuration to `config/pipeline.yaml`:

```yaml
sources:
  custom_source:
    enabled: true
    api_endpoint: https://api.example.com
    api_key: ${CUSTOM_API_KEY}
    fetch_params:
      limit: 100
      category: ai
```

### Adding New Enrichment Steps

Extend the enrichment process in `pipeline/enrich.py`:

```python
def enrich_item_advanced(item):
    # Standard enrichment
    enriched = enrich_item(item)
    
    # Additional enrichment
    enriched['trending_score'] = llm.calculate_trending_score(item.content)
    enriched['impact_level'] = llm.assess_impact(item.content)
    enriched['prerequisites'] = llm.extract_prerequisites(item.content)
    
    return enriched
```

## Monitoring and Alerting

### Pipeline Status Monitoring
Add monitoring to track:
- Fetch success rates per source
- Enrichment processing time
- Deduplication statistics
- PR submission success rate
- Error rates and types

### Alerting
Set up alerts for:
- Pipeline failures
- High error rates (>10%)
- PR submission failures
- API rate limiting issues
- LLM enrichment failures

## Testing

### Unit Tests
Test individual components:

```bash
# Test fetchers
pytest tests/test_fetchers.py

# Test enrichment
pytest tests/test_enrichment.py

# Test deduplication
pytest tests/test_deduplication.py
```

### Integration Tests
Test the full pipeline:

```bash
# Run pipeline in test mode
pipeline run --all --dry-run --test-mode

# Test with sample data
pipeline run --source test --sample-file tests/sample_data.json
```

## Performance Optimization

### Caching
Implement caching for:
- API responses (respect rate limits)
- LLM enrichment results
- Deduplication comparisons

### Parallel Processing
Run fetchers in parallel:
```python
from concurrent.futures import ThreadPoolExecutor

def run_fetchers_parallel(fetchers):
    with ThreadPoolExecutor(max_workers=len(fetchers)) as executor:
        results = list(executor.map(lambda f: f.fetch(), fetchers))
    return results
```

## Troubleshooting

### Common Issues

**Issue**: LLM enrichment fails
- **Solution**: Check LM Studio is running on localhost:1234
- **Solution**: Verify Gemma 4 model is loaded
- **Solution**: Check API endpoint configuration

**Issue**: GitHub API rate limiting
- **Solution**: Implement proper rate limiting
- **Solution**: Use authentication tokens
- **Solution**: Add delays between requests

**Issue**: Deduplication too aggressive
- **Solution**: Adjust similarity threshold in config
- **Solution**: Review fuzzy matching algorithm
- **Solution**: Add manual override for specific items

## Contributing

### Adding New Data Sources
1. Implement fetcher following the pattern in `pipeline/fetchers/`
2. Add tests in `tests/test_fetchers.py`
3. Update documentation
4. Submit PR to DataPipeline repository

### Improving Enrichment
1. Experiment with different LLM prompts
2. Add new enrichment fields
3. Improve categorization accuracy
4. Submit PR with improvements

### Bug Fixes
1. Identify issue in pipeline logs
2. Write test case reproducing the bug
3. Fix the issue
4. Verify fix with tests
5. Submit PR

## Future Enhancements

### Planned Features
- **Multi-model enrichment**: Support for multiple LLMs
- **Image generation**: Add image model fetchers
- **Video content**: Include video resource fetchers
- **Community submissions**: Allow community-suggested resources
- **Quality scoring**: Add community rating system
- **Trending analysis**: Real-time trending resource detection

### Integration Improvements
- **Automated testing**: Run tests on each PR
- **Preview environment**: Preview changes before PR submission
- **Rollback capability**: Easy rollback of problematic additions
- **Analytics dashboard**: Pipeline performance monitoring

## Support

For issues or questions about the DataPipeline:
1. Check existing issues in the repository
2. Review troubleshooting section
3. Open new issue with detailed description
4. Include logs and configuration if applicable

The DataPipeline is critical for keeping the Awesome-AGI-and-ASI repository current with the latest developments in the rapidly evolving AGI/ASI landscape.