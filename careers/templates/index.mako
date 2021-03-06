<%inherit file="layout.mako"/>
{% block content %}

    {% if paginator.items %}

        <h2>Blog entries</h2>

        <ul>
            {% for entry in paginator.items %}
                <li>
                    <a href="{{ request.route_url('blog', id=entry.id, slug=entry.slug) }}">
                        {{ entry.title }}
                    </a>
                </li>
            {% endfor %}
        </ul>

        {{ paginator.pager() |safe }}

    {% else %}

        <p>No blog entries found.</p>

    {% endif %}

    <p><a href="{{ request.route_url('blog_action',action='create') }}">
        Create a new blog entry</a></p>

{% endblock %}